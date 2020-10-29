from Get_one_book import *
from main import *

table_items = [get_product_page_url(), get_product_upc(article), get_title(article)]
with open('projet2.csv', 'w') as P2_test:
    csv_writer = csv.writer(P2_test, delimiter='')
    csv_writer.writerow(['Product_page_url', 'product_upc', 'title'])
    csv_writer.writerow(table_items)