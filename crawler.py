import requests
import bs4

url = input("url: ")
response = requests.get(url)
print(type(response))
print(response.text)


