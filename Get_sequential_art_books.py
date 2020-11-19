from bs4 import BeautifulSoup
import requests

#ul class pager, li class next et il y a le lien dedans


def get_category_book(category_url):
    response = requests.get(category_url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'lxml')
    category_url = list()
    for link in soup.find_all('h3'):
        category_url.append(link.a.attrs['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))
    print(category_url)


#get_category_book("https://books.toscrape.com/catalogue/category/books/sequential-art_5/")

def get_category_books(category_url):
    response = requests.get(category_url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'lxml')
    category_url = list()
    for next_button in soup.find_all("li"):
        category_url.append(next_button.a.href.replace('../../../', 'http://books.toscrape.com/catalogue/'))
        print(category_url)


get_category_books("https://books.toscrape.com/catalogue/category/books/sequential-art_5/")

    #Dans cette boucle soup.find.all('h3)





#tant que next existe chercher els infos avec url
#créer dossier pour chaque catégorie bibli os ?
#dossier dedans avec image où on met l'ensemble des images des livres



        #mettre dans une liste et chercher dans les differentes pages
        #liste de livre et dico de catégorie
   #récupérer url d'une page puis boucle pour plusieurs pages
   #va chercher tant qu'il y a un next parse les livres
   #titrer le csv avec le nom de la catégorie
   #refaire cours sur les fonction avec le passage en argument (input)
    #Puis on met toutes les url dans un dico
    #On parse les infos de chaque url de la liste
    #On envoie ces infos vers un nouveau csv

