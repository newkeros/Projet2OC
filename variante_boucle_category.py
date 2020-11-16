from bs4 import BeautifulSoup
import requests


def category_book_loop():
    for i in range(5):  # la liste cherche à partir de 0, on a 4 pages à scraper
        categories_url = []  # On crée la liste
        url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-" + str(i) + ".html"
        response = requests.get(url)
        print(response)
        if response.ok:  # considérée réponse ok = 200
            print('page : ' + str(i))
            soup = BeautifulSoup(response.text, 'lxml')
            all_h3 = soup.find_all('h3')
            for h3 in all_h3:
                a = h3.find('a')
                link = a['href']
                categories_url.append('https://books.toscrape.com/catalogue' + link)
    print(categories_url)
    with open('sequential_art_cat_links.txt', 'w') as file:
        for link in categories_url:
            file.write(link + '\n')


category_book_loop()
