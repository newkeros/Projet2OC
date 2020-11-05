def get_all_product_infos():
    product_infos = {}
    product_infos["product_page_url"] = get_product_page_url()
    product_infos["product_upc"] = get_product_upc(article)
    product_infos["title"] = get_title(article)
    product_infos["price_including_tax"] = get_price_including_tax(article)
    product_infos["price_excluding_tax"] = get_price_excluding_tax(article)
    product_infos["number_available"] = get_number_available(article)
    product_infos["product_description"] = get_product_description(article)
    product_infos["category"] = get_category(article)
    product_infos["review_rating"] = get_review_rating(article)
    product_infos["image_url"] = get_image_url(article)
    return (product_infos)