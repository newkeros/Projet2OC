from bs4 import BeautifulSoup
import requests

# request va récupérer les données html
r = requests.get("http://books.toscrape.com/catalogue/how-music-works_979/index.html")
# BS va récupérer le texte avec lxml pour parser les infos
soup = BeautifulSoup(r.text, 'lxml')
# On cherche ce qu'on veut avec soup.find dans le code html
article = soup.find('article')

# print(article.prettify())

#title = article.find('div', class_='col-sm-6 product_main').h1.text
#print(title)
table_infos = len(article.find('table', class_='table table-striped'))
print(table_infos[0,1,4,5,6,7])
#product_description = article.find('div', class_='sub-header').h2.text
#print(product_description)
#product_description_text = article.find('div', id_='product_description')
#print(product_description_text)
