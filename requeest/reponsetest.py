import requests
one = {"q":"pizza"}
r = requests.get("https://www.google.com", params=one)
print("status:", r.status_code)
f= open("./pages.html", "w+")
f.write(r.text)
