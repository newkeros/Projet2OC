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


def get_price_excluding_tax(article):
    price_without_tax = article.select("tr")
    print(price_without_tax[2].td.text)


def get_number_available(article):
    number_available = article.select("p")
    print(number_available[1].text.strip())


def get_category(article):
    category = article.select("tr")
    print(category[1].td.text)


def get_review_rating(article):
    review_rating = article.find_all('p')[2]
    print(review_rating.get("class")[-1])
    # Utiliser methode join() ?

def get_review_rating2(article):
    review_rating2 = article.select('div')
    print(review_rating2[6].p)


def get_image_url(article):
    get_image = article.find_all("img")[0]
    print(get_image.get("src"))
    #A retravailler pour cleaner



#nouvelle fonction pour créer dictionnaire avec get product

