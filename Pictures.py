import requests


def get_picture(dico_key):
    response = requests.get(dico_key["image_url"])

    with open(category_dict["title"], "wb") as file:
        file.write(response.content)
    print(response)