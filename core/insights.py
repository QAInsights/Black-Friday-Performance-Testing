import requests
import csv
import json
import time


from core.write_to_influx import write_to_influx_cloud



def get_insights(site, key, bucket, influxkey, influxurl, influxorg):
    """
    Get Page Speed Insights for each site
    @param bucket:          Influx bucket name
    @param influxkey:       Influx API key
    @param influxurl:       Influx Cloud URL
    @param influxorg:       Influx Org name
    @param key:             PageSpeed Insights API Key
    @param site:            Website URL
    """
    try:
        url = "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url=https%3A%2F%2F" + str(site) + \
              "&category=PERFORMANCE&strategy=DESKTOP" + "&key=" + key
        print("Checking the insights of " + url)

        # Compose Headers
        headers = {
            'content-type': 'application/json'
        }
        time.sleep(2)

        # Send URL
        req = requests.get(url, headers=headers, timeout=30)
        # Receive response and convert into JSON
        res = json.loads(req.text)
        try:
            # Fetch Time
            # fetch_time = str(res['lighthouseResult']['fetchTime'])
            # Getting Current time stamp in ms
            fetch_time = int(round(time.time() * 1000))
            # Lab Data
            # Print FCP
            fcp = str(res['lighthouseResult']['audits']['first-contentful-paint']['displayValue'])
            # Print Speed Index
            si = str(res['lighthouseResult']['audits']['speed-index']['displayValue'])
            # Time To Interactive
            toi = str(res['lighthouseResult']['audits']['interactive']['displayValue'])
            # First Meaningful Paint
            fmp = str(res['lighthouseResult']['audits']['first-meaningful-paint']['displayValue'])
            # First CPU Idle
            # fci = str(res['lighthouseResult']['audits']['first-cpu-idle']['displayValue'])
            # Estimated Input Latency
            # eil = str(res['lighthouseResult']['audits']['estimated-input-latency']['displayValue'])

            # Field Data
            # LARGEST_CONTENTFUL_PAINT_MS
            field_lcp = str(res['loadingExperience']['metrics']['LARGEST_CONTENTFUL_PAINT_MS']['percentile'])
            # FIRST_CONTENTFUL_PAINT_MS
            field_fcp = str(res['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['percentile'])
            # FIRST_INPUT_DELAY_MS
            field_fid = str(res['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['percentile'])
            # CUMULATIVE_LAYOUT_SHIFT_SCORE
            field_cls = str(res['loadingExperience']['metrics']['CUMULATIVE_LAYOUT_SHIFT_SCORE']['percentile'])

            with open('results.csv', 'a+', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['URL', 'FETCH_TIME', 'FCP', 'TOI', 'SI', 'FMP', 'FIRST_CONTENTFUL_PAINT_MS',
                              'FIRST_INPUT_DELAY_MS',
                              'LARGEST_CONTENTFUL_PAINT_MS', 'CUMULATIVE_LAYOUT_SHIFT_SCORE']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({
                    'URL': site,
                    'FETCH_TIME': fetch_time,
                    'FCP': fcp,
                    'TOI': toi,
                    'SI': si,
                    'FMP': fmp,
                    # 'EIL': fci,
                    # 'CLS': eil,
                    'FIRST_CONTENTFUL_PAINT_MS': field_fcp,
                    'FIRST_INPUT_DELAY_MS': field_fid,
                    'LARGEST_CONTENTFUL_PAINT_MS': field_lcp,
                    'CUMULATIVE_LAYOUT_SHIFT_SCORE': field_cls
                }
                )
            csvfile.close

            # "responsetime,url=www.gg.com fcp=0.5,toi=1.2,si=0.5,fmp=0.5"
            line_protocol_data = "responsetime,url=" + site + " " + "fcp=" + fcp.split()[0] + ",toi=" + toi.split()[
                0] + ",si=" + si.split()[0] + ",fmp=" + fmp.split()[0]
            write_to_influx_cloud(bucket, influxkey, influxurl, influxorg, line_protocol_data)
        except KeyError:
            pass
    except requests.exceptions.Timeout as e:
        print(e)
