#error not resolved
from bs4 import BeautifulSoup
import requests
search = input("search for:")
params = {"q":"search"}
r = requests.get("http://www.google.com/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_content"})
links = soup.findAll("li", {"class": "b_algo"})
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
