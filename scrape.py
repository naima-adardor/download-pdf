import requests
from bs4 import BeautifulSoup

# Load your email HTML content
html_content = """
<html lang="en"><head>
\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><style type="text/css">
\n<!--
\n-->
\n</style><style type="text/css">
\n<!--
\n-->
\n</style><style type="text/css">
\n<!--
\na[x-apple-data-detectors]
\n	{color:inherit!important;
\n	font-size:inherit!important;
\n	font-family:inherit!important;
\n	font-weight:inherit!important;
\n	line-height:inherit!important}
\n#MessageViewBody a
\n	{color:inherit;
\n	text-decoration:none;
\n	font-size:inherit;
\n	font-family:inherit;
\n	font-weight:inherit;
\n	line-height:inherit}
\n#MessageViewBody
\n	{margin:0 auto!important}
\n-->
\n</style><style type="text/css">
\n<!--
\na, body, table, td, th
\n	{box-sizing:border-box!important}
\ntable, td
\n	{}
\nimg
\n	{border:0;
\n	height:auto;
\n	line-height:100%;
\n	outline:0;
\n	text-decoration:none}
\nbody
\n	{height:100%!important;
\n	margin:0!important;
\n	padding:0!important;
\n	width:100%!important}
\np
\n	{margin-top:8px;
\n	margin-bottom:16px}
\n@media only print and (max-width: 600px) {
\nbody
\n	{max-width:320px}
\n
\n	}
\n@media all and (max-width: 600px) {
\n.outerContainer
\n	{width:100%!important}
\n.innerContainer
\n	{padding-left:0!important;
\n	padding-right:0!important}
\n.fullWidth
\n	{width:100%!important;
\n	display:block}
\nu ~ div #full-wrap
\n	{min-width:100vw}
\nh1.hero-h1
\n	{font-size:36px!important;
\n	line-height:45px!important}
\nh1.hero-h1_variable
\n	{font-size:130%!important;
\n	line-height:135%!important}
\nh2.body-h2
\n	{font-size:24px!important;
\n	line-height:30px!important}
\nh3.body-h3
\n	{font-size:20px!important;
\n	line-height:24px!important}
\nh3.body-h3-link
\n	{font-size:20px!important;
\n	line-height:24px!important}
\nh4.body-h4-link
\n	{font-size:14px!important;
\n	line-height:18px!important}
\nh1.h1-xl
\n	{font-size:44px!important;
\n	line-height:55px!important}
\nh1.h1-lg
\n	{font-size:36px!important;
\n	line-height:45px!important}
\nh1.h1-md
\n	{font-size:28px!important;
\n	line-height:35px!important}
\nh1.h1-sm
\n	{font-size:24px!important;
\n	line-height:30px!important}
\nh1.h1-xs
\n	{font-size:20px!important;
\n	line-height:28px!important}
\nh2.h2-xl
\n	{font-size:28px!important;
\n	line-height:35px!important}
\nh2.h2-lg
\n	{font-size:24px!important;
\n	line-height:30px!important}
\nh2.h2-md
\n	{font-size:20px!important;
\n	line-height:28px!important}
\nh2.h2-sm, h2.h2-xs
\n	{font-size:16px!important;
\n	line-height:24px!important}
\nh3.h3-xl, h3.h3-link-xl
\n	{font-size:24px!important;
\n	line-height:30px!important}
\nh3.h3-lg, h3.h3-link-lg
\n	{font-size:20px!important;
\n	line-height:28px!important}
\nh3.h3-md, h3.h3-link-md
\n	{font-size:16px!important;
\n	line-height:24px!important}
\nh3.h3-sm, h3.h3-xs, h3.h3-link-sm, h3.h3-link-xs
\n	{font-weight:normal!important;
\n	font-size:16px!important;
\n	line-height:24px!important}
\np.body-p-lg
\n	{font-size:36px!important;
\n	line-height:43px!important}
\np.body-p-sm
\n	{font-size:14px!important;
\n	line-height:22px!important}
\np.body-p-xs
\n	{font-size:12px!important;
\n	line-height:20px!important}
\n.ph-0
\n	{padding-left:0px!important;
\n	padding-right:0px!important}
\n.p-0
\n	{padding:0px!important}
\n.pt-0
\n	{padding-top:0px!important}
\n.pr-0
\n	{padding-right:0px!important}
\n.pb-0
\n	{padding-bottom:0px!important}
\n.pl-0
\n	{padding-left:0px!important}
\n.pb-4
\n	{padding-bottom:4px!important}
\n.pt-4
\n	{padding-top:4px!important}
\n.ph-8
\n	{padding-left:8px!important;
\n	padding-right:8px!important}
\n.pb-8
\n	{padding-bottom:8px!important}
\n.ptb-8
\n	{padding-top:8px!important;
\n	padding-bottom:8px!important}
\n.pt-8
\n	{padding-top:8px!important}
\n.pl-8
\n	{padding-left:8px!important}
\n.pl-10
\n	{padding-left:10px!important}
\n.pr-8
\n	{padding-right:8px!important}
\n.pb-12
\n	{padding-bottom:12px!important}
\n.ph-15
\n	{padding-left:15px!important;
\n	padding-right:15px!important}
\n.pr-15
\n	{padding-right:15px!important}
\n.pl-15
\n	{padding-left:15px!important}
\n.pb-15
\n	{padding-bottom:15px!important}
\n.ph-16
\n	{padding-left:16px!important;
\n	padding-right:16px!important}
\n.pt-16
\n	{padding-top:16px!important}
\n.pr-16
\n	{padding-right:16px!important}
\n.pb-16
\n	{padding-bottom:16px!important}
\n.pl-16
\n	{padding-left:16px!important}
\n.p-16
\n	{padding-top:16px!important;
\n	padding-right:16px!important;
\n	padding-bottom:16px!important;
\n	padding-left:16px!important}
\n.pt-20
\n	{padding-top:20px!important}
\n.ph-20
\n	{padding-left:20px!important;
\n	padding-right:20px!important}
\n.p-20
\n	{padding-top:20px!important;
\n	padding-right:20px!important;
\n	padding-bottom:20px!important;
\n	padding-left:20px!important}
\n.pt-24
\n	{padding-top:24px!important}
\n.pr-24
\n	{padding-right:24px!important}
\n.pb-24
\n	{padding-bottom:24px!important}
\n.pl-24
\n	{padding-left:24px!important}
\n.p-24
\n	{padding-top:24px!important;
\n	padding-right:24px!important;
\n	padding-bottom:24px!important;
\n	padding-left:24px!important}
\n.ph-24
\n	{padding-right:24px!important;
\n	padding-left:24px!important}
\n.pb-27
\n	{padding-bottom:27px!important}
\n.ph-30
\n	{padding-left:30px!important;
\n	padding-right:30px!important}
\n.pt-30
\n	{padding-top:30px!important}
\n.pb-30
\n	{padding-bottom:30px!important}
\n.pt-32
\n	{padding-top:32px!important}
\n.pb-32
\n	{padding-bottom:32px!important}
\n.ph-32
\n	{padding-left:32px!important;
\n	padding-right:32px!important}
\n.pt-36
\n	{padding-top:36px!important}
\n.pr-36
\n	{padding-right:36px!important}
\n.pb-36
\n	{padding-bottom:36px!important}
\n.pl-36
\n	{padding-left:36px!important}
\n.pt-37
\n	{padding-top:37px!important}
\n.pt-38
\n	{padding-top:38px!important}
\n.pt-40
\n	{padding-top:40px!important}
\n.pb-40
\n	{padding-bottom:40px!important}
\n.show
\n	{display:block!important;
\n	max-height:none!important;
\n	overflow:visible!important}
\n.hide
\n	{display:none!important}
\n.hide-bg
\n	{background-image:none!important}
\n.bt-1
\n	{border-top:1px solid\n#f6f6f6!important}
\n.bt-0
\n	{border-top:0px solid #fff!important}
\n.bt-15
\n	{border-top:15px solid #fff!important}
\n.bb-5
\n	{border-bottom:5px solid\n#f6f6f6!important}
\n.br-0
\n	{border-right:none!important}
\n.bgcolor-m
\n	{background-color:#f6f6f6!important}
\n.bgcolor-white-m
\n	{background-color:#ffffff!important}
\n.width-100
\n	{width:100%!important}
\n.width-70
\n	{width:70%!important}
\n.width-50
\n	{width:50%!important}
\n.center
\n	{margin:0 auto!important}
\n.center-align-text
\n	{text-align:center!important}
\n.left-align-text
\n	{text-align:left!important}
\n.stack
\n	{display:block!important}
\n.table
\n	{display:table!important}
\n.cta.stack a
\n	{width:100%!important}
\n.height-580
\n	{height:300px!important;
\n	background-position:bottom!important}
\n.no-border
\n	{border:none!important;
\n	border-radius:0!important}
\n.h24
\n	{height:24px!important}
\n.h16
\n	{height:16px!important}
\n.jobCardLabels
\n	{margin:0 0 4px!important;
\n	width:100%!important;
\n	display:block!important}
\n.radius8
\n	{border-radius:8px!important}
\n.eml_BasicTable_HideOnMobile
\n	{display:none!important}
\n
\n	}
\n@media only screen and (min-width: 600px) {
\n.eml_BasicTable_MobileShow
\n	{display:none!important}
\n
\n	}
\n-->
\n</style></head><body class="darkmode-bg-weak" alink="#2557a7" link="#2557a7" vlink="#2557a7" bgcolor="#f3f2f1" style="margin:0; padding:0"><div style="display:none; max-height:0px; overflow:hidden">Alexander Higuita Sanchez applied</div><div style="display:none; max-height:0px; overflow:hidden"> ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­ ͏­</div><table class="full-wrap darkmode-bg-weak" cellpadding="0" cellspacing="0" border="0" align="center" bgcolor="#f3f2f1" width="100%" role="presentation" style="min-width:100%"><tbody><tr><td align="center" valign="top" class="pt-0" style="padding:15px 0 0"><table class="outerContainer darkmode-bg-base" cellpadding="0" cellspacing="0" border="0" align="center" bgcolor="#ffffff" width="100%" role="presentation" style="max-width:600px"><tbody><tr><td align="center" valign="top"><table class="darkmode-bg-base" cellpadding="0" cellspacing="0" border="0" align="left" bgcolor="#ffffff" width="100%" role="presentation"><tbody><tr><td align="center" valign="top" class="pr-24 pl-10 darkmode-border-weak" style="padding:0 56px 0 42px; border-bottom:0"><table cellpadding="0" cellspacing="0" border="0" align="left" width="100%" role="presentation"><tbody><tr><td align="center" valign="top" style="padding:0px"><table cellpadding="0" cellspacing="0" border="0" align="left" width="100%" role="presentation"><tbody><tr><td class="darkmode-logo-padding" align="left" valign="middle"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_4WQMU_DMBCF_wrywETTMIBQJAsJBgaqsBQxRq59TY7YPmOfFaqq_x03GWBBHd9933vDHUUWjRiYQ2rW62maKvQGwFSaqjyuB4zwqPlbglNoV7vsjQXTqRAsasVIvpvJNSY0l6Vxkv_TzK5LlKOGMhQsHSAuJM3IgcHs5K-rlQsKe39hMkRp4lLwLBMyzIEPAaRFP87JkpYOzaKRfHkSN8KJ5ih0WRy3Q6TcD-VRHDMUtFzLQjltqKerTRlaza2gInjejoWcEyV-_iO_t6_t20dbCJ-N28_7XX23H74IOT_UtTidfgCDRV9fkQEAAA/QXfjf45CX96rCBuBduoKIONDfApV3CM8PyRqWzrEfhA"><img src="https://prod.statics.indeed.com/eml/assets/images/logo/ForEmployers_GB_en_color_horizontal_whitebg.png" alt="Indeed for Employers" width="auto" height="52" class="darkmode-logo-hide" style="font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; color:#004fcb; font-size:20px; display:block; width:auto; height:52px; max-height:52px"> <img src="https://prod.statics.indeed.com/eml/assets/images/logo/ForEmployers_GB_en_white_horizontal.png" alt="Indeed for Employers" width="auto" height="23" class="darkmode-logo-show darkmode-t-primary" style="font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; color:#004fcb; font-size:20px; display:none; width:auto; height:23px; max-height:23px"> </a></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><table class="darkmode-bg-weak full-wrap" cellpadding="0" cellspacing="0" border="0" align="center" bgcolor="#f3f2f1" width="100%" role="presentation" style="min-width:100%"><tbody><tr><td align="center" valign="top"><table class="darkmode-border-weak darkmode-bg-base outerContainer" cellpadding="0" cellspacing="0" border="0" align="center" bgcolor="#ffffff" width="100%" role="presentation" style="max-width:600px; width:600px; border-top:1px solid #e4e2e0"><tbody><tr><td align="center" valign="top"><table class="darkmode-bg-base innerContainer" cellpadding="0" cellspacing="0" border="0" align="left" bgcolor="#ffffff" width="100%" role="presentation" style="max-width:600px"><tbody><tr><td align="center" valign="top" class="ph-16" style="padding:40px 56px 0px"><table cellpadding="0" cellspacing="0" border="0" align="left" width="100%" role="presentation" style="min-width:100%"><tbody><tr><td align="left" style="padding:8px 0 0"><h1 class="darkmode-t-strong h1-md" style="color:#2d2d2d; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:20px; font-weight:bold; line-height:30px; margin:0; padding:0; direction:ltr"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_02PTW-CQBCG_0qzB04iEKNBEtKDxyb0oul5YAcY3S-XWVtj_O9dQpt4nPd5JvPOQwRRiZHZTVWWoXbK3tFPazISUa47q7MOjCQJjFN2I_x-J1m37WZXFiXKYr9NPPanmBXnXZtvezCDDfsy3yQd_9SogVQKzinqgMmaREVVg4EBU2vS5UzSe6vrFytd9iKlG8kASqyEFtVDdNG4HEdvwzDG3uwDRrSkd4cxOvy3fWtAz9CBR8PHS2TzZCc-vOin5qP5_Goi4dn4e2K8WuJQ5rl4Pn8BH3htvSIBAAA/ivA86x6Td5I-aWE-FTYAKXxqC6BKDDuC4jANFUQv7bI" style="text-decoration:underline; color:#2d2d2d">Alexander Higuita Sanchez</a> applied</h1></td></tr><tr><td align="left" style="padding:4px 0 24px"><p class="darkmode-t-base" style="color:#595959; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:14px; font-weight:normal; line-height:21px; margin:0; padding:0; direction:ltr">Junior Broker • London EC3A</p></td></tr><tr><td align="left"><table cellpadding="0" cellspacing="0" border="0" role="presentation"><tbody><tr><td style="list-style-type:none; padding:0 0 0 0"><p style="color:#2d2d2d; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:14px; font-weight:normal; line-height:21px; margin:0; padding:0; direction:ltr">Relevant experience: Junior Trader at Artemis Funds</p></td></tr><tr><td style="padding:16px 0 8px 0"><p style="color:#2d2d2d; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:14px; font-weight:bold; line-height:21px; margin:0; padding:0; direction:ltr">Qualifications</p></td></tr><tr><td><table align="left" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" role="presentation" style="border-radius:8px; margin:4px 4px 0 0; float:left; border:1px solid #e4e2e0"><tbody><tr><td style="padding:3px 8px 3px 8px"><table cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" role="presentation"><tbody><tr><td align="center" valign="middle"><p style="color:#2d2d2d; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:14px; line-height:21px; margin:0; padding:0; direction:ltr">Work authorisation</p></td></tr></tbody></table></td></tr></tbody></table><table align="left" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" role="presentation" style="border-radius:8px; margin:4px 4px 0 0; float:left; border:1px solid #e4e2e0"><tbody><tr><td style="padding:3px 8px 3px 8px"><table cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" role="presentation"><tbody><tr><td align="center" valign="middle"><p style="color:#2d2d2d; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:14px; line-height:21px; margin:0; padding:0; direction:ltr">Interview availability</p></td></tr></tbody></table></td></tr></tbody></table><table align="left" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" role="presentation" style="border-radius:8px; margin:4px 4px 0 0; float:left; border:1px solid #e4e2e0"><tbody><tr><td style="padding:3px 8px 3px 8px"><table cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" role="presentation"><tbody><tr><td align="center" valign="middle"><p style="color:#2d2d2d; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:14px; line-height:21px; margin:0; padding:0; direction:ltr">Willingness to travel</p></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td class="pb-32" align="left" valign="top" style="padding:0px"><table cellpadding="0" cellspacing="0" border="0" align="center" width="100%" role="presentation"><tbody><tr><td align="left" style="padding:24px 0 0"><table class="width-100" cellpadding="0" cellspacing="0" border="0" align="left" role="presentation"><tbody><tr><td align="center" class="stack cta center-align-text" style="border-radius:12px; border:2px solid #ffffff"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_02PzW6DMBCEXwX5wKkEUJSIIKGq6rERPTRRz4u9wBb_xdhpoyjvXkdUao47883u7JUFVrPRezvXeY7KSnNBN69IC0Sx4kblHLQgAR7n_Ez4_Uyi6br1tiorFOVukzrsj1Erv7ZdselBDybsqmKdcv_ToAKSGVgriYMno1MZUQUaBsyMzpYzae-Mah6obMlFl84kAkj2xBSrr4xHYjqMzoRhjL29CxitRb1YjNIHYtIHKZOX_3XJnvQUOQsOtT9MEbtPZvavD8lj-9a-f7bR8Xfi75_xZMiHqijY7fYLjNYjry0BAAA/tOHRCcGw7UeYaVS-y4narYYhKDeld3EYa0KQOM0xkFI" class="primary-button darkmode-ta-inverse darkmode-bga-primary" style="background-color:#004fcb; font-size:16px; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-weight:bold; text-decoration:none; padding:12px 16px; color:#ffffff; display:block; border-radius:12px; min-width:272px; width:auto; direction:ltr"><span style="">See full application </span></a></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td><table align="left" cellpadding="0" cellspacing="0" border="0" width="100%" role="presentation"><tbody><tr><td align="left" class="stack cta center-align-text" valign="top" style="padding:12px 0 0"><div><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_02QbW-CMBSF_4ohcZ-mokyjLmaRiW46cDhf-VbpRSqUIrTzLf73XXUfbJrm3vOckzTnrCmtrYVSpnm7UgGexuIIWV5mCQWgZV_wik8SyiiRkFcyyBWHtwyCGaOd6rax1usBSTZCtZq68UR4-op693pWtGe-nJbe4oOHc16s9eOFp7ti5xtN-Apcy5uSlrXe2nYEhpwsl1tbDQJFTEpzVzrS7VsNa9nyVo3dAsP-8bP5zcatFfDjilWLNbPr41MbGIdh3Up-en0zxn1uD8cw9KbbvUMxNYp5ZE6IgdY-T-aADoYjYYOxnZ7cotHDe_u1Lw8d4ITFJZKmMfOJZCK5kSATvPMglu427If9MqpIrD1rXGufNR8d0TTMhNqEWKnMFCC6q8cUUJoz2BfuFRZilkSIU5JBIqcR0usmcvn-EJg5I2e8cJDIq-O_73AnmFRNXdculz_gRcOWvwEAAA/ayqNQYVYOsGr3emJhM1wcu8YZyER6WqDhICnZKMKTqI" style="background-color:#ffffff; border-radius:8px; color:#2d2d2d; display:inline-block; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:16px; font-weight:bold; line-height:44px; padding:0 16px; text-align:center; text-decoration:none; width:auto; min-width:272px; direction:ltr">View CV <img src="https://prod.statics.indeed.com/eml/assets/images/icons/ArrowRight_black_whitebg.png" alt="" width="20" style="vertical-align:text-bottom; line-height:0px; padding:0 8px 0 0; width:20px"></a> </div></td></tr></tbody></table></td></tr><tr><td aria-hidden="true" class="" height="28" align="center" valign="top" style="height:28px; font-size:28px; line-height:28px">&nbsp;</td></tr><tr><td><p style="display:none; color:#ffffff; margin:0; padding:8px 0 0; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:14px; font-weight:normal">This is an application update about a candidate who applied to your job </p></td></tr><tr><td class="" align="center" valign="top" aria-hidden="true" style="padding:0 0 0px; border-top:1px solid #e4e2e0; line-height:0; width:100%">&nbsp;</td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><table class="darkmode-bg-weak full-wrap" cellpadding="0" cellspacing="0" border="0" align="center" bgcolor="#f3f2f1" width="100%" role="presentation" style="min-width:100%"><tbody><tr><td align="center" valign="top"><table class="outerContainer darkmode-bg-weak" cellpadding="0" cellspacing="0" border="0" align="center" bgcolor="#ffffff" width="100%" role="presentation" style="max-width:600px; width:600px"><tbody><tr><td align="center" valign="top" class="p-24" style="padding:32px 56px"><table cellpadding="0" cellspacing="0" border="0" align="left" width="100%" role="presentation"><tbody><tr><td align="left" valign="top" style="padding:0px"><table cellpadding="0" cellspacing="0" border="0" align="left" width="100%" role="presentation"><tbody><tr><td align="left" valign="top" style="padding:0px 0px 24px; border-bottom:1px solid #e4e2e0"><p class="darkmode-t-base" style="color:#595959; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:12px; font-weight:normal; line-height:18px; margin:0; padding:0; direction:ltr"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_02PMW-DMBCF_0rkgakJDqiEIKEOHdPSJVFnY87gALZrn6uiKP-9l6ZDtrv3vrund2GRVWxAdKFKU5jdZBfwYaNNB9BtpJ1TIaWNBskUekqdBwUejITwQuNJd_X2XLT8WQnT27gveZ5I_Kn_6LVwbtJSoLYmUd7O9YOwviOUpL91F8WUUBIeYKmLVvGy2Il8D7LIil2Xt-1WqqwrVSZznrEnNrPqwiS9Go-Dt7EfqAX6CGTd1cUBSe_CiB5WARC16cPqTZuRECeoAR5HIm6bDfj6cHRqDs3HZ0MO3oj_esOX1RhLztn1-gtuWCg4NgEAAA/lz1TS7lvKuJqvieeVsNaH21kT9mQni385epF6v6l64c" style="color:#595959; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:12px; font-weight:normal; line-height:21px; margin:0; padding:0; direction:ltr; text-decoration:underline">Manage application update settings</a><br>No longer want application emails for this job? Ask the person who posted the job or your account admin to remove you from these application updates. <br><br>By replying or using an indeedemail.com address, you acknowledge that the email conversation will become part of the corresponding Indeed Messaging thread and will be processed and analysed according to Indeed's <a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_4WQQUvEMBCF_4pE8KS2HhQpBME9eBCqhxWPJU1mN2ObTEwmaln2v5ttBb3IHt_7vnmH2YksGmGZQ2qqykYGbUPED6WnS02u6qPyJlXoDYC50_wlwSkcL_rszQimUyGMqBUj-W4mZ5jQHJeGT_k_zey6RDlqKENhpAniQtKMHBjMTv66WrmgcOuPTIYoTVwOPMuEDHPgKYAc0Q9zGklLh2bRSD7cn66IBoQkzoUTzU7osjysbaS8teV1HDMUtLRlqVQ_ByfPVMqpwKAieF4PhR0SJV790V_ax_bptS2ED8bV201fX2_sOyHn27oW-_03fyxfi6UBAAA/2hv38QCoM_2UfUT1ZmcBDEuirtaYooi2ehPY8yS3Rz4" style="text-decoration:underline; color:#595959">Cookie Policy</a>, <a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_4WQPU_DMBRF_wrywAQkHUAokoUEA0Ol0KGIMXLs1_oRf2E_A1HV_44bD7Cgjvee8-7wDiyzjmmikLqm0ZFA6hDxU8j5RnrbjFE4lRp0CkA9SPrmYAWa6zE7ZUANIgSDUhB6NyzkEhOq89L0xf-nmeyQfI4SylAwfoZYSVqQBYXZ8l9XChsE7t2ZyRC5ivXAEU9IsASaA3CDblqS8ZJbVFXz_PmRXTHLugOTZXHa6ujzXpeXUcxQUG3LQqk29W8XG1_KucAgIjjaToWdkk_09Ed_7df9y1tfCJ2M1fvd2N7u9IdHyvdty47HH4F5JImdAQAA/sCNnVk4x6WT0kDJa7eYI5OxqmO0aWTf7j8JzuJPK5QE" style="text-decoration:underline; color:#595959">Privacy Policy</a>, and <a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_4WQT0vEMBDFv8oSoSfd1oMihSCshz0I9WDFY8kms-3Y_DOZqMuy3920RfQie5s3vzdvhjmyxGo2EPlYl-V2s0arANRaOlNq6IW-l_TFwQjUV7tklQbVCe81SkHobDeTAiOq86bxk_9PE5kuuhQk5CCv3QHCQuKMDChMhv96pTBeYG_PRPrAVVgGLPGIBLOggweu0Y6z0k5yg2qxOb7dFIPmYIu5vvg5J7JLZlh9ZDLvGdshuNQP-XkUEmS0dHNubrUQTFy5_eoZwgfKCXsRwFI7ZjopF-nhz8BL89g8vTaZ0OS4frvdVTf74d0hpbuqYqfTN-MDsNKpAQAA/lxDc3fiSsqDyIVlYecyeEBC8TxhwpiHDbFW6d3tWHIg" style="text-decoration:underline; color:#595959">Terms of Service</a>.</p></td></tr></tbody></table><table cellpadding="0" cellspacing="0" border="0" align="left" width="100%" role="presentation"><tbody><tr><td align="left" class="fullWidth pb-24" style="padding:24px 0px 0px"><table cellpadding="0" cellspacing="0" border="0" align="left" width="100%" role="presentation"><tbody><tr><td align="left" valign="top" style="padding:0px 0px 12px"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_4WQPU_DMBRF_4sHJpqkAwhFspDogCqksBQxRq79aB7-xH5WqKr-d1xngAV1vPecd4d3Ypn1bCIKqW_beZ4bdApANdI3WbePkr45WIFmtc9OGVCjCMGgFITejZXcYEJ1XdIz_59msmPyOUooQ8H4I8SFpIosKMyW_7pS2CDw4K5MhshVXA4c8YQENdAxADfodE3GS25RLZrnz0_sllnWn5gsi3o3RZ8PU3kSxQwFLW1ZKNW2_mpVT4KI4GinS31JPtHmj_k2vAyv70MhdDHWn_f77u5j-vJI-aHr2Pn8AwzrX2WKAQAA/I-whfwlloUYjJzz9eyJv7d-9LJUFsy0FzJwbyyagz04"><img src="https://prod.statics.indeed.com/eml/assets/images/logo/indeed_en_color.png" alt="Indeed home" width="80" class="darkmode-logo-hide" style="font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; color:#004fcb; font-size:20px"> <img src="https://prod.statics.indeed.com/eml/assets/images/logo/indeed_en_white.png" alt="Indeed home" width="80" class="darkmode-logo-show darkmode-t-primary" style="font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; color:#004fcb; font-size:20px; display:none"> </a></td></tr><tr><td align="left" valign="top" class="fullWidth pb-16" style="padding:0px"><p class="darkmode-t-base" style="color:#595959; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:12px; font-weight:normal; line-height:18px; margin:0; padding:0; direction:ltr">© 2025 Indeed UK Operations Ltd.<br>20 Farringdon Road | 3rd floor | London EC1M 3HE | United Kingdom<br><br>Indeed Ireland Operations Limited Block B, Capital Dock, 80 Sir John Rogerson's Quay, Grand Canal Dock, Dublin 2, D02&nbsp;HE36, Ireland</p><p class="darkmode-t-base" style="color:#595959; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:12px; font-weight:normal; line-height:18px; margin:12px 0 0; padding:0; direction:ltr">Indeed processes and analyses your activity in this email.</p></td></tr></tbody></table></td><td align="left" class="fullWidth left-align-text pt-20 pb-36" valign="top" style="padding:24px 0px 0px"><table class="fullWidth" cellpadding="0" cellspacing="0" border="0" align="right" role="presentation"><tbody><tr><td align="right" valign="top" class="pl-0" style="padding:0px 8px 0px  0px"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_02MsQ6CMBRF_-XNSuugMR01agxJXSDOUIotFVrLaxpD-HdLdHC895x7JwjAQCG6kRESY8zaSsjaWpMJ2xM9NFI2ZX49EVhBD2wC8dTCFMrb8FBpij7IhL7t28lUnX8P68shEVd5OWBhEliSHfH455Y857c7TwQXY9Ptarpt1ctqDHtKYZ4_n7_89qIAAAA/gbTvZLDnHxHQEWqMSb1Q3jdACP6CWjGWEuvGBko5tR0" class="darkmode-ta-primary" style="color:#004fcb; text-decoration:underline; font-size:12px"><img src="https://prod.statics.indeed.com/eml/assets/images/icons/Facebook_black_whitebg.png" alt="Indeed's Facebook" width="24" class="darkmode-logo-hide"> <img src="https://prod.statics.indeed.com/eml/assets/images/icons/Facebook_white_blackbg.png" alt="Indeed's Facebook" width="24" class="darkmode-logo-show" style="display:none"> </a></td><td align="left" valign="bottom" class="fullWidth left-align-text" style="padding:0px 8px 0px"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_02MvQrCMBRG3-XO2tRBkYw6iAhxqTinadrEmh-TG4KUvrspIjh-5xy-CRJQUIg-UkJyzpW2EfkQuKmEM0TbTsqud6FNUVsZI4EVGKATiKcWY6OCS4MqFxiSLOpL314WdP49rU-HojwP0mIzFrMsF_H4F9_YhV3vrBhcis1j19bbXr2cxrSva5jnD1-YK7KrAAAA/MgKbYtyhepiCEq7tpgkPs6_1zutcAMFdqCW2ABOdIuw" class="darkmode-ta-primary" style="color:#004fcb; text-decoration:underline; font-size:12px"><img src="https://prod.statics.indeed.com/eml/assets/images/icons/Instagram_black_whitebg.png" alt="Indeed's Instagram" width="24" class="darkmode-logo-hide"> <img src="https://prod.statics.indeed.com/eml/assets/images/icons/Instagram_white_blackbg.png" alt="Indeed's Instagram" width="24" class="darkmode-logo-show" style="display:none"> </a></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td align="left" valign="top" class="" style="padding:24px 0px 0px"><table cellpadding="0" cellspacing="0" border="0" align="left" role="presentation"><tbody><tr role="list"><th align="left" class="fullWidth br-0" role="listitem" style="padding:0 8px 0 0; border-right:1px solid #595959"><p class="darkmode-t-base" style="color:#595959; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:16px; font-weight:normal; line-height:18px; margin:0; padding:0; direction:ltr"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_4WQPU_DMBRF_4sHJpqkAwhFspDogCqksBQxRq79aB7-xH5WqKr-d1xngAV1vPecd4d3Ypn1bCIKqW_beZ4bdApANdI3WbePkr45WIFmtc9OGVCjCMGgFITejZXcYEJ1XdIz_59msmPyOUooQ8H4I8SFpIosKMyW_7pS2CDw4K5MhshVXA4c8YQENdAxADfodE3GS25RLZrnz0_sllnWn5gsi3o3RZ8PU3kSxQwFLW1ZKNW2_mpVT4KI4GinS31JPtHmj_k2vAyv70MhdDHWn_f77u5j-vJI-aHr2Pn8AwzrX2WKAQAA/I-whfwlloUYjJzz9eyJv7d-9LJUFsy0FzJwbyyagz04" class="darkmode-ta-primary" style="color:#004fcb; text-decoration:underline; font-size:12px">Indeed</a></p></th><th align="left" class="fullWidth pt-24 br-0 pl-0" role="listitem" style="padding:0 8px; border-right:1px solid #595959"><p class="darkmode-t-base" style="color:#595959; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:16px; font-weight:normal; line-height:18px; margin:0; padding:0; direction:ltr"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_4WQP0_DMBTEvwrywERJGEAokoUEQ4dKoUMRY-TYj_oR_8N-BqKq3x3XGWBBHe9-dzfcgWXWMU0UUtc0OhJIHSJ-CjlfS2-bMQqnUoNOAagHSd8crECzGrNTBtQgQjAoBaF3QyWXmFCdD01f_H-ayQ7J5yihDAXjZ4gLSRVZUJgt_81KYYPAvTszGSJXcSk44gkJqqA5ADfopqqMl9yiWmKerx_ZFbOsOzBZFqedjj7vdbmMYoaCFrcsFGu7_Hax9cWcV7UaRARHu6ngk_KJnv40XvpN__zaF0KnxM373djevukPj5Tv25Ydjz--AV6LoAEAAA/aYFn9kmaAJKso0Z7djM_OrBZM9ErfDAqzbo1UdHJzTI" class="darkmode-ta-primary" style="color:#004fcb; text-decoration:underline; font-size:12px">Privacy Policy</a></p></th><th align="left" class="fullWidth pt-24 br-0 pl-0" role="listitem" style="padding:0 8px; border-right:1px solid #595959"><p class="darkmode-t-base" style="color:#595959; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:16px; font-weight:normal; line-height:18px; margin:0; padding:0; direction:ltr"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_4WQT0vEMBDFv0uEnna39aBIIQj10INQLxWPJZuM7dj822SCLst-d7MtohfZ27z3e_Mm5MQSq9lE5GNdlm2zQ6sA1E46U2oYhX6U9MXBCNTbfbJKgxqE9xqlIHR2WEiBEdX10PzJ_6eJzBBdChJykdfuCGElcUEGFCbDf7NSGC9wtFcqfeAqrAuWeESCRdDRA9do50VpJ7lBtcYcb5ti0hxsscw3P8-JbMMMq09M5jtzPwWXxil_HoUEGa1u7s1WD8HEbdtk24sAlvo5uxflIj39Cb52z93LW5cJXRK3H_f76u59Ojik9FBV7Hz-Bg-S4cuhAQAA/vYix811a82Zji1ybwj-G-NnlAjGRbpmyyAtqgQTzMUE" class="darkmode-ta-primary" style="color:#004fcb; text-decoration:underline; font-size:12px">Terms</a></p></th><th align="left" class="fullWidth pt-24 br-0 pl-0" role="listitem" style="padding:0 8px; border-right:none"><p class="darkmode-t-base" style="color:#595959; font-family:'Indeed Sans','Noto Sans',Helvetica,Arial,sans-serif; font-size:16px; font-weight:normal; line-height:18px; margin:0; padding:0; direction:ltr"><a href="https://cts.indeed.com/v1/H4sIAAAAAAAA_4WQzU7DMBCE38WHnmiSHopQJAupHIpUKRwo4hi59pIs8R_2WhBVfXecRAguqMeZb3Y96zNLrGY9kY91WaJVAAqtLMxYRCQopDMlGK_dCOE5ee8CbcpY3kv64mAE6vUpWaVBtcJ7jVIQOtvOZIUR1fXQ8Mn_p4lMG10KEvhPi4XEGZlcNhn-m5XCeIGdvbLSB67CMmCJT4fOgkYPXKMdZqWd5AbVEnN8v1tpYbskutzFtvsdu2GG1Wcm8wPDsQ8udX3-SwoJMlrcvDBbj6D9eh7wIoCl45DNSblID39yL82heXptMqEpsXm_PVXbt_7DIaW7qmKXyzcRypDlrwEAAA/uM6Hbm7nOitFVfzbhUQdnorq92YMBckDS2DoigBHpgg" class="darkmode-ta-primary" style="color:#004fcb; text-decoration:underline; font-size:12px">Help Centre</a></p></th></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><img border="0" width="1" height="1" alt="" src="https://engage.indeed.com/q/R-O3fYZjHm6nNjfozQ8jbA~~/AAR9hBA~/x5bzjFc1K-uCgImY5TtwkzMkW6Lyzxg9Uf5PdlW_PTc-0iO5kectXW1TGeWrrI3S1GHmAhr2D-FdYgXOIKy8fQ~~"> </body></html>
"""

# Parser le HTML
soup = BeautifulSoup(html_content, "html.parser")

# 1️⃣ Nom du candidat
name_tag = soup.find("h1")
candidate_name = name_tag.get_text(strip=True).replace(" applied", "") if name_tag else None

# 2️⃣ Poste et lieu
position_tag = soup.find("p", class_="darkmode-t-base")
position_location = position_tag.get_text(strip=True) if position_tag else None

# 3️⃣ Expérience pertinente
experience_tag = soup.find("p", string=lambda t: t and "Relevant experience:" in t)
experience = experience_tag.get_text(strip=True).replace("Relevant experience: ", "") if experience_tag else None

# 4️⃣ Qualifications (liste)
qualifications = []
qual_tags = soup.find_all("p", string=lambda t: t and t in ["Work authorisation", "Interview availability", "Willingness to travel"])
for q in qual_tags:
    qualifications.append(q.get_text(strip=True))

# 5️⃣ Lien vers le CV / candidature complète
cv_link_tag = soup.find('a', string='View CV')
cv_link = cv_link_tag['href'] if cv_link_tag else None

# Affichage
print("Nom :", candidate_name)
print("Poste & Lieu :", position_location)
print("Expérience :", experience)
print("Qualifications :", qualifications)
print("Lien CV :", cv_link)
