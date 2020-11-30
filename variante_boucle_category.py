from bs4 import BeautifulSoup
import requests

def category_book_loop():
    for i in range(1, 5):  # la liste cherche à partir de 0, on a 4 pages à scraper
        url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-" + str(i) + ".html"
        response = requests.get(url)
        print(i)
        while response.ok:
            # considérée réponse ok = 200
            print('page : ' + str(i))
            break
        soup = BeautifulSoup(response.text, 'lxml')
        all_h3 = soup.find_all('h3')
        categories_url = list()
        for h3 in all_h3:
            a = h3.find('a')
            link = a['href']
            categories_url.append('https://books.toscrape.com/catalogue/' + link.strip("../../.."))
    print(categories_url)

    with open('sequential_art_cat_links.txt', 'w') as file:
        for link in categories_url:
            file.write(link + '\n')


category_book_loop()


"""def test_cat_urls(categories_url):
    i = 1
    categories_url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-1.html"
    while True:
        i = i + 1
        page = requests.get(categories_url)
        if page.status_code != 200:
            break
        categories_url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-" + str(i) + "html"
        response = requests.get(categories_url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'lxml')
        categories_url = list()
        for link in soup.find_all('h3'):
            categories_url.append(link.a.attrs['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))
            break
    print(categories_url)"""
