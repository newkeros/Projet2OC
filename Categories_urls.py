from bs4 import BeautifulSoup
import requests

def collect_categories_urls():
    """base_url = website_url
    next_category = True
    categories_urls = list()
    i = 1
    while next_category:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.text, 'lxml')
        for link in soup.find_all('li'):
            categories_urls.append(link.a.attrs['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))
        next_category = soup.find("li", {"a": "href"}) is not None
        i += 1
        category_url = base_url + "page-" + str(i) + ".html"
        catalogue / category / books / sequential - art_5 / index.html
    return books_urls"""


response = requests.get("https://books.toscrape.com/index.html")
soup = BeautifulSoup(response.text, 'lxml')
get_categories_urls = soup.find_all('a')[2:53]
print(get_categories_urls.get("href"))