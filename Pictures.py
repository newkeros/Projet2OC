import requests
from parserbook import get_all_product_infos


def get_picture(category_dict):
    response = requests.get(category_dict["image_url"])

    with open(category_dict["image_filename"], "wb") as file:
        file.write(response.content)
        return category_dict