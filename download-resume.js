const express = require('express');
const bodyParser = require('body-parser');
const puppeteer = require('puppeteer'); // <== ici

const app = express();
app.use(bodyParser.json());

app.post('/download-resume', async (req, res) => {
  const { url } = req.body;

  if (!url) return res.status(400).send('URL is required');

  try {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle0' });

    const pdf = await page.pdf({ format: 'A4' });
    await browser.close();

    res.setHeader('Content-Type', 'application/pdf');
    res.send(pdf);
  } catch (err) {
    console.error(err);
    res.status(500).send('Error generating PDF');
  }
});

app.listen(3001, () => console.log('Server listening on http://localhost:3001'));
