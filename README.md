# 🎯 Objective

The objective of this exercise is to measure the response time trend of popular US retail websites during Thanksgiving and Black Friday 2020.

# 🔝 Strategy

This experiment **will not inject load** to the websites under test. The script will **send only one HTTP(S) request every 30 minutes** to measure the performance. The actual workload will be from the real users.

# 🌐 List of Websites under test

Here are the [URLs](urls.yaml) which will be tested. If you would like to add any other websites, please submit a PR.

# 🔧 Tools

- [Page Speed Insights](https://developers.google.com/speed/docs/insights/v5/about)
- Python scripts
- GitHub Actions
- Influx DB Cloud

# ⌛ Test Window

Test will start at 12.00 AM EST on Nov 28 and ends at 12.01 AM EST Nov 30.

# 🔢 Results

Results will be published after collating the results tentatively by 06.00 PM EST on Nov 30.

# 📊 Performance Metrics

Following metrics will be captured:

 - First Contentful Paint (FCP)
 - First Input Delay (FID)
 - Largest Contentful Paint (LCP)
 - Cumulative Layout Shift (CLS)