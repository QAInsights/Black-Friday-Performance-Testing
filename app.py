import yaml
import argparser
from core.insights import get_insights

def main():
    """
    The main context.
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
    with open('urls.yaml') as url:
        url = yaml.safe_load(url)
        for site in url['Websites']:
            get_insights(site,key)
        

if __name__ == "__main__":
    main()