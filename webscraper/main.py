from bs4 import BeautifulSoup
import requests
search = input("enter search term:")
params = {"q":search}
r = requests.get("http://www.bing.com/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())

