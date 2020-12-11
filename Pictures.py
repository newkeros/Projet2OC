from requests import request

response = request.get(url)

file = open("sample_image.png", "wb")
file.write(response.content)
