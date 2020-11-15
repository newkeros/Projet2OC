from bs4 import BeautifulSoup
import requests

def category_book_loop():
    for i in range(5):  #la liste cherche à partir de 0, on a 4 pages à scraper
        categories_url = []  #On crée la liste
        url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-" + str(i) + ".html"
        response = requests.get(url)
        print(response)
        if response.ok:  #considérée réponse ok = 200
            print('page : ' + str(i))
            soup = BeautifulSoup(response.text, 'lxml')
            all_h3 = soup.find_all('h3')
            for h3 in all_h3:
                a = h3.find('a')
                link = a['href']
                categories_url.append('https://books.toscrape.com/catalogue' + link)
    print(len(categories_url))


    #with open('sequential_art_cat_links.txt', 'w') as file:
        #for link in categories_url:
            #file.write(link + '\n')






"""def get_category_book(category_url):
    response = requests.get(category_url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'lxml')
    article = soup.find('article')
    categories_url = list()
    for link in soup.find_all('h3'):
        categories_url.append(link.a.attrs['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))

    print(categories_url)"""


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

