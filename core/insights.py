import requests
import csv
import json

def get_insights(site):
    """
    Get Page Speed Insights for each site
    @param site: Website URL    
    """
    url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://" + str(site) + \
            "&key=AIzaSyC7vcN8DTFge3OFUDSGNyYhhbiOHmnbRVQ" + "&strategy=DESKTOP"
    print(url)
    # Send URL
    req = requests.get(url)
    # Receive response and convert into JSON
    res = json.loads(req.text)

    # Fetch Time
    fetch_time = str(res['lighthouseResult']['fetchTime'])

    # Lab Data
    #Print FCP
    fcp = str(res['lighthouseResult']['audits']['first-contentful-paint']['displayValue'])
    #Print Speed Index
    si = str(res['lighthouseResult']['audits']['speed-index']['displayValue'])
    #Time To Interactive
    toi = str(res['lighthouseResult']['audits']['interactive']['displayValue'])
    #First Meaningful Paint
    fmp = str(res['lighthouseResult']['audits']['first-meaningful-paint']['displayValue'])
    #First CPU Idle
    fci = str(res['lighthouseResult']['audits']['first-cpu-idle']['displayValue'])
    #Estimated Input Latency
    eil = str(res['lighthouseResult']['audits']['estimated-input-latency']['displayValue'])
    
    #print(fcp + si + toi + fmp + fci + eil)

    #Field Data 
    #LARGEST_CONTENTFUL_PAINT_MS
    field_lcp = str(res['loadingExperience']['metrics']['LARGEST_CONTENTFUL_PAINT_MS']['percentile'])

    #FIRST_CONTENTFUL_PAINT_MS
    field_fcp = str(res['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['percentile'])

    #FIRST_INPUT_DELAY_MS
    field_fid = str(res['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['percentile'])

    #CUMULATIVE_LAYOUT_SHIFT_SCORE
    field_cls = str(res['loadingExperience']['metrics']['CUMULATIVE_LAYOUT_SHIFT_SCORE']['percentile'])

    #print(field_cls + "score" + field_lcp + "ms" +  field_fcp + "ms" + field_fid + "ms")

    with open('results.csv','a+',newline='') as csvfile:
        fieldnames = ['URL','FETCH_TIME','FCP','TOI','SI','FMP','EIL','CLS','FIRST_CONTENTFUL_PAINT_MS','FIRST_INPUT_DELAY_MS',
                        'LARGEST_CONTENTFUL_PAINT_MS','CUMULATIVE_LAYOUT_SHIFT_SCORE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'URL': site,
            'FETCH_TIME': fetch_time,
            'FCP':fcp,
            'TOI':toi,
            'SI':si,
            'FMP':fmp,
            'EIL':fci,
            'CLS':eil,
            'FIRST_CONTENTFUL_PAINT_MS': field_lcp,
            'FIRST_INPUT_DELAY_MS': field_fid,
            'LARGEST_CONTENTFUL_PAINT_MS': field_fcp,
            'CUMULATIVE_LAYOUT_SHIFT_SCORE': field_cls                
        }            
        )            
    csvfile.close