# File for creating csv file

from Get_one_book import *
from csv import DictWriter

def create_csv():
    with open('testproject01.csv', 'a', newline='') as f:
        all_data = get_all_product_infos()
        fieldnames = ["product_page_url", "product_upc", "title", "price_including_tax", "price_excluding_tax",
                      "number_available", "product_description", "category", "review_rating", "image_url"]
        csv_writer = DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerow(all_data)