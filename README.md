[![contributions welcome](https://img.shields.io/badge/contributions-welcome-1EAEDB)]()
[![saythanks](https://img.shields.io/badge/say-thanks-1EAEDB.svg)](https://saythanks.io/to/catch.nkn%40gmail.com)
[![](https://img.shields.io/badge/license-MIT-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-QAInsights-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://qainsights.com)
[![](https://img.shields.io/badge/%E2%9D%A4-YouTube%20Channel-0a0a0a.svg?style=flat&colorA=1EAEDB)](https://www.youtube.com/user/QAInsights?sub_confirmation=1)
[![](https://img.shields.io/badge/donate-paypal-1EAEDB)](https://www.paypal.com/paypalme/NAVEENKUMARN)

# 🎯 Objective

The objective of this exercise is to measure the response time trend of popular US retail websites during Thanksgiving and Black Friday 2021. This will help us to reveal the performance and its effect of retain giants.  

# 🔝 Strategy

This experiment **will not inject load** to the websites under test. The script will **send only one HTTP(S) request every 30 minutes** to measure the performance. The actual workload will be from the real users.

HTTP request timeout is set to 30 seconds. If the script doesn't receive any response from Page Speed, then that request will be ignored. 

Only the desktop performance will be captured.

# 🌐 List of Websites under test

Here are the [URLs](urls_bf.yaml) which will be tested. If you would like to add any other websites, please submit a PR.

# 🔧 Tools

- [Page Speed Insights](https://developers.google.com/speed/docs/insights/v5/about)    
- Python 3.9
- GitHub Actions
    - Chrome browser
    - Ubuntu latest
- Influx DB Cloud (Free Plan)

# ⌛ Test Window

Test will start at 12.00 AM EST on Nov 25 and ends at 12.01 AM EST Nov 30.

# 🔢 Results

Results will publish instantly to InfluxDB cloud. 

# 📊 Performance Metrics

Following metrics will be captured:

 - First Contentful Paint (FCP)
 - First Input Delay (FID)
 - Largest Contentful Paint (LCP)
 - Cumulative Layout Shift (CLS)
 
 # 👩‍🍳 How to set up this experiment on your own?
 
 * Clone this repo
 * Install the requirements using `pip install -r requirements.txt`
 * Grab a Page Speed Insights API from [here](https://developers.google.com/speed/docs/insights/v5/get-started).
 * Create GitHub secrets for the following. For instructions, please check [here](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets). Never ever expose your API key in your repo.
   * `API_KEY` - PageSpeed API key
   * `BUCKET_NAME` - Influx DB bucket name
   * `INFLUX_API_KEY` - Influx DB API key
   * `INFLUX_URL` - Influx DB cloud URL
   * `INFLUX_ORG` - Influx Org name
 * In your `.github/workflows/python-app.yml` file, configure your details in the line 41 and 42.
 * By default, GitHub Action will get triggered on every push.
 * To schedule the run for every 15 minutes, use the below config in the yaml file.
```
 on:
  schedule:
    # * is a special character in YAML so you have to quote this string
    - cron:  '*/15 * * * *'
```

 # ❓ FAQs

 * Can I view the performance realtime?
    - Yes. Using the Influx DB cloud, the results will get published instantly.
 * What is the cost involved in this experiment?
    - Nothing. All are using free resources.😊
