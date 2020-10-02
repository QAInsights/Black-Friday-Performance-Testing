import yaml
from core.insights import get_insights

def main():
    """
    The main context.
    """
    with open('urls.yaml') as url:
        url = yaml.safe_load(url)
        for site in url['Websites']:
            get_insights(site)
        

if __name__ == "__main__":
    main()