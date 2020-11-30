from bs4 import BeautifulSoup
import requests


def get_category_books(category_url):
    base_url = category_url[:-10]
    next_flag = True
    books_urls = list()
    i = 1
    while next_flag:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.text, 'lxml')
        for link in soup.find_all('h3'):
            books_urls.append(link.a.attrs['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))
        next_flag = soup.find("li", {"class": "next"}) is not None
        i += 1
        category_url = base_url + "page-" + str(i) + ".html"
    print(books_urls)

#autre fonction qui va appeler à partir de la liste get_Category_books
#créer un csv par category
#utiliser module OS pour créer les dossiers dans lequel il ya aura les urls en csv + dossier images
#dans un dossier data qui contiendra les dossiers de toutes les catégories
#fonction create folder + creer folder au nom de la catégorie
#dans la fonction csv mettre focntion telecharchement images

get_category_books("https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")

"""def get_category_books(category_url):
    response = requests.get(category_url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'lxml')
    category_url = list()
    for next_button in soup.find_all("li"):
        category_url.append(next_button.a.href.replace('../../../', 'http://books.toscrape.com/catalogue/'))
        print(category_url)"""


#get_category_books("https://books.toscrape.com/catalogue/category/books/sequential-art_5/")

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

