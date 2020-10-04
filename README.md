[![contributions welcome](https://img.shields.io/badge/contributions-welcome-1EAEDB)]()
[![saythanks](https://img.shields.io/badge/say-thanks-1EAEDB.svg)](https://saythanks.io/to/catch.nkn%40gmail.com)
[![](https://img.shields.io/badge/license-MIT-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-QAInsights-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-YouTube%20Channel-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://www.youtube.com/user/QAInsights?sub_confirmation=1)
[![](https://img.shields.io/badge/donate-paypal-1EAEDB)](https://www.paypal.com/paypalme/NAVEENKUMARN)

# 🎯 Objective

The objective of this exercise is to measure the response time trend of popular US retail websites during Thanksgiving and Black Friday 2020. This will help us to reveal the performance and its effect of retain giants.  

# 🔝 Strategy

This experiment **will not inject load** to the websites under test. The script will **send only one HTTP(S) request every 30 minutes** to measure the performance. The actual workload will be from the real users.

HTTP request timeout is set to 30 seconds. If the script doesn't receive any response from Page Speed, then that request will be ignored. 

Only the desktop performance will be captured.

# 🌐 List of Websites under test

Here are the [URLs](urls.yaml) which will be tested. If you would like to add any other websites, please submit a PR.

# 🔧 Tools

- [Page Speed Insights](https://developers.google.com/speed/docs/insights/v5/about)    
- Python 3.8
- GitHub Actions
    - Chrome browser
    - Ubuntu 18.04 LTS
- Influx DB Cloud (Free Plan)

# ⌛ Test Window

Test will start at 12.00 AM EST on Nov 28 and ends at 12.01 AM EST Nov 30.

# 🔢 Results

Results will be published after collating the results tentatively by 06.00 PM EST on Dec 01.

# 📊 Performance Metrics

Following metrics will be captured:

 - First Contentful Paint (FCP)
 - First Input Delay (FID)
 - Largest Contentful Paint (LCP)
 - Cumulative Layout Shift (CLS)

 # ❓ FAQs

 * Can I view the performance realtime?
    - No. The setup doesn't include that. But you can download the raw results anytime once the experiement started and analyze it yourself.
 * What is the cost involved in this experiement?
    - Nothing. All are using free resources.😊
 * Can I setup this experiment on my own?
    - Yes. Please raise a PR if you are really interested.