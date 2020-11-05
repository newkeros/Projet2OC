from typing import Union

from bs4 import BeautifulSoup, NavigableString
import requests

response = requests.get("http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, 'lxml')
article = soup.find('article')

def get_seq_arts_books():

    #Dans un premier temps on récupère toutes les urls
    #pseudo-code Lit le href dans col-xs-6 col-sm-4 col-md-3 col-lg-3
    # Si col-xs-6 col-sm-4 col-md-3 col-lg-3 existe printe le href
    # Passe au prochain col-xs-6 col-sm-4 col-md-3 col-lg-3 et applique condition
    # Arrete boucle quand plus de col-xs-6 col-sm-4 col-md-3 col-lg-3 à lire
    soup.select("col-xs-6 col-sm-4 col-md-3 col-lg-3")
    page = article.find('a')['href']
    print(page.replace('../../..', 'http://books.toscrape.com/catalogue'))

    #Puis on met toutes les url dans un dico
    #On parse les infos de chaque url de la liste
    #On envoie ces infos vers un nouveau csv

get_seq_arts_books()

