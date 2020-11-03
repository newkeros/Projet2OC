from csv import DictWriter

from bs4 import BeautifulSoup
import requests
from CSV_creator import *
from Get_one_book import *

if __name__ == "__main__":
    # request va récupérer les données html
    r = requests.get("http://books.toscrape.com/catalogue/how-music-works_979/index.html")
    r.encoding = "utf-8"
    # BS va récupérer le texte avec lxml pour parser les infos
    soup = BeautifulSoup(r.text, 'lxml')
    # On cherche ce qu'on veut avec soup.find dans le code html
    article = soup.find('article')

    get_product_page_url()
    get_product_upc(article)
    get_title(article)
    get_price_including_tax(article)
    get_price_excluding_tax(article)
    get_number_available(article)
    get_product_description(article)
    get_category(article)
    get_review_rating(article)
    get_image_url(article)


    # ici ces fonctions disparaissent et il n'y aura que get product qui retourne un dico

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
        return(product_infos)


    def create_csv():
        with open('testproject01.csv', 'a', newline='') as f:
            all_data = get_all_product_infos()
            fieldnames = ["product_page_url", "product_upc", "title", "price_including_tax", "price_excluding_tax",
                          "number_available", "product_description", "category", "review_rating", "image_url"]
            csv_writer = DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerow(all_data)



    create_csv()
