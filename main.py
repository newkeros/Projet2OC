from bs4 import BeautifulSoup
import requests
from csv import DictWriter
from Get_one_book import get_all_product_infos
from Get_category_books import *
from CSV_creator import create_csv

import os

if __name__ == "__main__":
  create_csv(get_all_product_infos("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"), "greg")
  create_csv(get_all_product_infos("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"), "greg")














