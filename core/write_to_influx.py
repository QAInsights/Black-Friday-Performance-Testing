from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


def write_to_influx_cloud(bucket, influxkey, influxurl, influxorg, data):
    with InfluxDBClient(url=influxurl, token=influxkey, org=influxorg, verify_ssl=False) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

        # data = "responsetime,url=www.gg.com fcp=0.5,toi=1.2,si=0.5,fmp=0.5"
        write_api.write(bucket, influxorg, data)
        # query = 'from(bucket: "BlackFriday2021") |> range(start: -1h)'
        # tables = client.query_api().query(query, org=influxorg)
        # for table in tables:
        #     for record in table.records:
        #         print(record)
        client.close()
