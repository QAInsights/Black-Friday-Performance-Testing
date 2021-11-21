import yaml
import argparse

from core.insights import get_insights


def main():
    """
    The main context.
    Start Time: 11/25 06.00 PM EST
    """
    parser = argparse.ArgumentParser(
        description='API Key'
    )
    required_named = parser.add_argument_group('mandatory arguments')
    required_named.add_argument(
        "-k",
        "--key",
        dest="apikey",
        help="Send API Key"
    )
    required_named.add_argument(
        "-b",
        "--bucket",
        dest="bucket",
        help="Influx Bucket name"
    )
    required_named.add_argument(
        "-i",
        "--influxkey",
        dest="influxkey",
        help="Send Influx API Key"
    )
    required_named.add_argument(
        "-u",
        "--influxurl",
        dest="influxurl",
        help="Send Influx Cloud URL"
    )
    required_named.add_argument(
        "-o",
        "--influxorg",
        dest="influxorg",
        help="Send Influx Org"
    )
    args = parser.parse_args()
    key = args.apikey
    bucket = args.bucket
    influxkey = args.influxkey
    influxurl = args.influxurl
    influxorg = args.influxorg

    with open('urls.yaml') as url:
        url = yaml.safe_load(url)
        for site in url['Websites']:
            get_insights(site, key, bucket, influxkey, influxurl, influxorg)


if __name__ == "__main__":
    main()
