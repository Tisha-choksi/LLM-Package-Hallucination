import urllib.request
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print(data)

def scrape_website(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    parser = MyHTMLParser()
    parser.feed(html)

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    scrape_website(url)