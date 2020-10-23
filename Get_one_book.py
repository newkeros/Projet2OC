from main import *

def get_product_page_url():
    page_url = str('http://books.toscrape.com/catalogue/how-music-works_979/index.html')
    print(page_url)


def get_title(article):
    title = article.find('div', class_='col-sm-6 product_main').h1.text
    print(title)


def get_product_upc(article):
    tableau = article.select("tr")
    print(tableau[0].td.text)


def get_product_description(article):
    product_description_text = article.select("p")
    print(product_description_text[3].text)


def get_price_including_tax(article):
    price_with_tax = article.select("tr")
    print(price_with_tax[3].td.text)

if __name__ == "__main__":
    # request va récupérer les données html
    r = requests.get("http://books.toscrape.com/catalogue/how-music-works_979/index.html")
    # BS va récupérer le texte avec lxml pour parser les infos
    soup = BeautifulSoup(r.text, 'lxml')
    # On cherche ce qu'on veut avec soup.find dans le code html
    article = soup.find('article')
    get_product_page_url()
    get_product_upc(article)
    get_title(article)
    get_price_including_tax(article)
    #get_price_excluding_tax(article)
    #get_number_available(article)
    get_product_description(article)
    #get_category(article)
    #get_review_rating(article)
    #get_image_url(article)