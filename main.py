from parserbook import get_all_product_infos
from Get_category_books import *
from CSV_creator import create_csv
from Pictures import get_picture




if __name__ == "__main__":

    category_url_list = get_category_books("https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
    for urls in category_url_list:
        category_dict = get_all_product_infos(urls)
        create_csv(category_dict, "Sequential art")
        get_picture(category_dict)














