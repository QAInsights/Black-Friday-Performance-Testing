import pandas as pd

df = pd.read_csv("results.csv")

#URL,FETCH_TIME,FCP,TOI,SI,FMP,EIL,CLS,FIRST_CONTENTFUL_PAINT_MS,FIRST_INPUT_DELAY_MS,LARGEST_CONTENTFUL_PAINT_MS,CUMULATIVE_LAYOUT_SHIFT_SCORE

lines = ["rs"
         + ",url=" + str(df["URL"][d])
         + " "
         + "fcp=" + str(df["FIRST_CONTENTFUL_PAINT_MS"][d]) + ","
         + "lcp=" + str(df["LARGEST_CONTENTFUL_PAINT_MS"][d])
         + " " + str(df["FETCH_TIME"][d]) for d in range(len(df))]

thefile = open('influx.txt', 'w')
for item in lines:
    thefile.write("%s\n" % item)