from bs4 import BeautifulSoup
import requests

response = requests.get("http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, 'lxml')
article = soup.find('article')

def get_seq_arts_books_page():
    for link in soup.find_all('h3'):
        return(link.a.attrs['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))


books_list = get_seq_arts_books_page()
for full_list in books_list:
    print(full_list)
#get_books_list = [books_list]
#print(get_books_list)
#books_list['sequencial_arts'] = get_seq_arts_books_page

        #mettre dans une liste et chercher dans les differentes pages
        #liste de livre et dico de catégorie
   #récupérer url d'une page puis boucle pour plusieurs pages
   #va chercher tant qu'il y a un next parse les livres
   #titrer le csv avec le nom de la catégorie
   #refaire cours sur les fonction avec le passage en argument (input)

    #print(page.replace('../../..', 'http://books.toscrape.com/catalogue'))
    #Puis on met toutes les url dans un dico
    #On parse les infos de chaque url de la liste
    #On envoie ces infos vers un nouveau csv

#get_seq_arts_books_page()

