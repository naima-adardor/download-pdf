// server.js
require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs-extra');
const path = require('path');
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');

puppeteer.use(StealthPlugin());

const COOKIE_FILE = process.env.COOKIE_FILE || path.join(__dirname, 'indeed_cookies.json');
const LOGIN_URL = 'https://employers.indeed.com/account/login';
const DASHBOARD_URL = 'https://employers.indeed.com';
const REFRESH_INTERVAL_MIN = parseInt(process.env.REFRESH_INTERVAL_MIN || '30', 10);

const app = express();
app.use(bodyParser.json());

/* ---------------- Utils cookies ---------------- */
async function saveCookies(cookies) {
  await fs.writeJson(COOKIE_FILE, cookies, { spaces: 2 });
  console.log('Cookies saved:', COOKIE_FILE);
}

async function loadCookies() {
  if (!await fs.pathExists(COOKIE_FILE)) return null;
  return await fs.readJson(COOKIE_FILE);
}

function sanitizeForPuppeteer(cookies) {
  return cookies
    .filter(c => c && c.name && c.value && c.domain)
    .map(c => ({
      name: c.name,
      value: c.value,
      domain: (c.domain || '').startsWith('.') ? c.domain.slice(1) : c.domain,
      path: c.path || '/',
      secure: typeof c.secure === 'boolean' ? c.secure : true,
      httpOnly: typeof c.httpOnly === 'boolean' ? c.httpOnly : false,
      expires: typeof c.expires === 'number' ? c.expires : undefined
    }));
}

/* ---------------- Vérifier validité session ---------------- */
async function isSessionValidWithCookies(cookies) {
  if (!cookies || cookies.length === 0) return false;
  
  try {
    const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
    const page = await browser.newPage();
    
    const sanitized = sanitizeForPuppeteer(cookies);
    await page.setCookie(...sanitized);
    
    await page.goto(DASHBOARD_URL, { waitUntil: 'networkidle2', timeout: 30000 });
    
    const url = page.url();
    await browser.close();
    
    // Si redirigé vers login, session invalide
    return !url.includes('/login') && !url.includes('/signin');
  } catch (err) {
    console.error('Session validation error:', err.message);
    return false;
  }
}

/* ---------------- Scheduler / Refresh cookies ---------------- */
async function refreshCookiesIfNeeded() {
  console.log('Checking cookies validity...');
  const cookies = await loadCookies();
  const valid = cookies ? await isSessionValidWithCookies(cookies) : false;

  if (valid) {
    console.log('Session still valid. No refresh needed.');
    return { refreshed: false, reason: 'still valid' };
  }

  console.log('Session invalid: automatic login skipped due to 2FA.');
  return { refreshed: false, reason: '2FA_required', message: 'Please login manually using /manual-login' };
}

/* ---------------- Login automatique ---------------- */
async function performLoginAndSaveCookies() {
  const email = process.env.EMPLOYER_EMAIL;
  const password = process.env.EMPLOYER_PASSWORD;
  if (!email || !password) throw new Error('ENV credentials missing (EMPLOYER_EMAIL / EMPLOYER_PASSWORD)');

  const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 900 });

  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36');

  await page.goto(LOGIN_URL, { waitUntil: 'networkidle2', timeout: 30000 });

  const emailSelector = 'input[type="email"], input[name="email"], input#email';
  const passwordSelector = 'input[type="password"], input[name="password"], input#password';
  const submitSelector = 'button[type="submit"], button:has-text("Sign in"), button:has-text("Se connecter")';

  await new Promise(resolve => setTimeout(resolve, 1500));
  await page.waitForSelector(emailSelector, { timeout: 10000 });

  await page.type(emailSelector, email, { delay: 50 });
  await page.type(passwordSelector, password, { delay: 50 });

  await Promise.all([
    page.click(submitSelector).catch(() => {}),
    page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 30000 }).catch(() => {})
  ]);

  const content = await page.content();
  if (/two-factor|2fa|authenticator|verification code|code de vérification|sms/i.test(content)) {
    await browser.close();
    throw new Error('2FA detected: automatic login cannot complete. Use manual login-flow.');
  }

  const cookies = await page.cookies();
  await saveCookies(cookies);
  await browser.close();
  return cookies;
}

/* ---------------- Login manuel (headful) ---------------- */
async function manualLoginAndSaveCookies() {
  const browser = await puppeteer.launch({ 
    headless: false, 
    args: ['--no-sandbox'], 
    defaultViewport: null 
  });
  const page = await browser.newPage();
  await page.goto(DASHBOARD_URL, { waitUntil: 'networkidle2' });

  console.log('Manual login started. Please complete login in the opened browser window.');
  console.log('After login, visit the /finish-manual-login endpoint to save cookies.');

  global.__manualLoginBrowser = browser;
  return { message: 'Manual browser opened. Complete login in the window, then call /finish-manual-login' };
}

/* ---------------- Scheduler pour rafraîchir ---------------- */
let refreshIntervalId = null;

function startAutoRefreshScheduler() {
  if (refreshIntervalId) return;
  refreshIntervalId = setInterval(async () => {
    try {
      await refreshCookiesIfNeeded();
    } catch (err) {
      console.error('Scheduler error:', err.message);
    }
  }, REFRESH_INTERVAL_MIN * 60 * 1000);
  console.log(`Cookie refresh scheduler started: every ${REFRESH_INTERVAL_MIN} minutes`);
}

/* ---------------- HTTP endpoints ---------------- */
app.post('/download-resume', async (req, res) => {
  const { url } = req.body;
  if (!url) return res.status(400).json({ error: 'URL required' });

  try {
    const cookies = await loadCookies();
    if (!cookies || cookies.length === 0) {
      return res.status(403).json({ error: 'No cookies saved. Please run /manual-login first.' });
    }

    const valid = await isSessionValidWithCookies(cookies);
    if (!valid) {
      return res.status(403).json({ error: 'Saved cookies invalid. Please login manually using /manual-login.' });
    }

    const browser = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 900 });

    // Appliquer les cookies
    const sanitized = sanitizeForPuppeteer(cookies);
    await page.setCookie(...sanitized);

    // Variable pour stocker le lien réel de téléchargement
    let downloadUrl = null;

    // Intercepter la requête réseau contenant le vrai lien
    page.on('request', request => {
      const reqUrl = request.url();
      if (reqUrl.includes('/api/catws/public/resume/download')) {
        downloadUrl = reqUrl;
        console.log('✅ Detected resume download URL:', downloadUrl);
      }
    });

    console.log('Navigating to resume URL...');
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });

    // Attendre le bouton "Télécharger"
    const downloadBtnSelector = 'a[data-testid="header-download-resume-button"]';
    await page.waitForSelector(downloadBtnSelector, { timeout: 15000 });
    console.log('✅ Download button found, clicking...');

    // Clic sur le bouton
    await page.click(downloadBtnSelector);
    await new Promise(resolve => setTimeout(resolve, 3000));

    await browser.close();

    if (!downloadUrl) {
      return res.status(500).json({ error: 'Failed to detect download URL. Possibly blocked or not logged in.' });
    }

    console.log('🎯 Final download URL:', downloadUrl);
    return res.json({ success: true, downloadUrl });

  } catch (err) {
    console.error('Download-resume error:', err);
    res.status(500).json({ error: err.message });
  }
});


app.get('/refresh-cookies', async (req, res) => {
  try {
    const result = await refreshCookiesIfNeeded();
    res.json(result);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/manual-login', async (req, res) => {
  try {
    const info = await manualLoginAndSaveCookies();
    res.json(info);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/finish-manual-login', async (req, res) => {
  try {
    const browser = global.__manualLoginBrowser;
    if (!browser) {
      return res.status(400).json({ error: 'No manual browser session found. Call /manual-login first.' });
    }
    
    const pages = await browser.pages();
    const page = pages[0] || await browser.newPage();
    
    // S'assurer qu'on est sur le bon domaine
    const currentUrl = page.url();
    console.log('Current URL:', currentUrl);
    
    if (!currentUrl.includes('indeed.com')) {
      console.log('Navigating to Indeed dashboard...');
      await page.goto(DASHBOARD_URL, { waitUntil: 'networkidle2', timeout: 30000 });
    }
    
    // Attendre un peu pour s'assurer que la connexion est établie
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    const cookies = await page.cookies();
    console.log('Cookies retrieved:', cookies.length);
    
    if (cookies.length === 0) {
      await browser.close();
      delete global.__manualLoginBrowser;
      return res.status(400).json({ 
        error: 'No cookies found. Make sure you are logged in to Indeed Employer and on the employers.indeed.com domain.' 
      });
    }
    
    await saveCookies(cookies);
    await browser.close();
    delete global.__manualLoginBrowser;
    
    res.json({ 
      message: 'Cookies saved from manual login', 
      cookiesCount: cookies.length 
    });
  } catch (e) {
    console.error('Finish manual login error:', e);
    res.status(500).json({ error: e.message });
  }
});

app.get('/start-scheduler', (req, res) => {
  startAutoRefreshScheduler();
  res.json({ message: 'Scheduler started' });
});

app.get('/stop-scheduler', (req, res) => {
  if (refreshIntervalId) clearInterval(refreshIntervalId);
  refreshIntervalId = null;
  res.json({ message: 'Scheduler stopped' });
});

app.get('/check-cookies', async (req, res) => {
  try {
    const cookies = await loadCookies();
    if (!cookies) {
      return res.json({ exists: false, count: 0 });
    }
    const valid = await isSessionValidWithCookies(cookies);
    res.json({ 
      exists: true, 
      count: cookies.length,
      valid: valid
    });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

/* ---------------- Start server ---------------- */
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
  console.log('Endpoints:');
  console.log('  - GET  /manual-login - Open browser for manual login');
  console.log('  - GET  /finish-manual-login - Save cookies after manual login');
  console.log('  - GET  /check-cookies - Check if cookies are saved and valid');
  console.log('  - POST /download-resume - Download resume as PDF');
  console.log('  - GET  /refresh-cookies - Check and refresh cookies');
  console.log('  - GET  /start-scheduler - Start auto-refresh scheduler');
  console.log('  - GET  /stop-scheduler - Stop auto-refresh scheduler');
});