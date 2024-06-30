import requests
from bs4 import BeautifulSoup

def get_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            links = soup.find_all('a')
            link_urls = [link.get('href') for link in links]

            return link_urls
        else:
            raise requests.exceptions.RequestException(f"Error an occurred: {response.status_code}")
    except requests.exceptions.RequestException as error:
        raise requests.exceptions.RequestException(f"Error an occurred: {str(error)}")

if __name__ == "__main__":
    url = input("Enter URL to scan for links: ")
    links = get_links(url)
    print("Links found on %s" % url)
    for link in links:
        print(link)
