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
    args = parser.parse_args()
    key = args.apikey
    with open('urls_bf.yaml') as url:
        url = yaml.safe_load(url)
        for site in url['Websites']:
            get_insights(site,key)
        

if __name__ == "__main__":
    main()