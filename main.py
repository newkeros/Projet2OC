from bs4 import BeautifulSoup
import requests
from csv import DictWriter
from Get_one_book import *

if __name__ == "__main__":
    # request va récupérer les données html
    response = requests.get("http://books.toscrape.com/catalogue/how-music-works_979/index.html")
    response.encoding = "utf-8"
    # BS va récupérer le texte avec lxml pour parser les infos
    soup = BeautifulSoup(response.text, 'lxml')
    # On cherche ce qu'on veut avec soup.find dans le code html
    article = soup.find('article')

    def get_all_product_infos():
        product_infos = {}
        product_infos["product_page_url"] = get_product_page_url()
        product_infos["product_upc"] = get_product_upc(article)
        product_infos["title"] = get_title(article)
        product_infos["price_including_tax"] = get_price_including_tax(article)
        product_infos["price_excluding_tax"] = get_price_excluding_tax(article)
        product_infos["number_available"] = get_number_available(article)
        product_infos["product_description"] = get_product_description(article)
        product_infos["category"] = get_category(article)
        product_infos["review_rating"] = get_review_rating(article)
        product_infos["image_url"] = get_image_url(article)
        return (product_infos)

    def create_csv():
        with open('testproject01.csv', 'w', newline='') as f:
            all_data = get_all_product_infos()
            fieldnames = ["product_page_url", "product_upc", "title", "price_including_tax", "price_excluding_tax",
                          "number_available", "product_description", "category", "review_rating", "image_url"]
            csv_writer = DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerow(all_data)


    #def get_all_category_infos
    #    with open('testproject01.csv', 'r') as csv_file:
    #        for row in csv_file:
    #            url = row.strip()
    #            response = requests.get(url)
    #                if response.ok:
    #                    soup = BeautifulSoup(response.text, 'lxml')
    #                   all_category_data = soup.find(get_all_product_infos())




    create_csv()


