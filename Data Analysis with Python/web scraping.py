import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup

def webscr(url):
    try:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html,'html.parser')

        # Retrieve all of the anchor tags
        tags = soup('a')
        for tag in tags:
            print(tag.get('href',None))
    except:
        raise ConnectionError('Connection Failed')

if __name__ == '__main__':
    webscr()