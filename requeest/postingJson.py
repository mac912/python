import requests
import json as simplejson
url= "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl":"http://example.com"}
headers = {"Content-Type":"application/json"}
r = requests.post(url, json = payload, headers= headers)
print(simplejson.loads(r.text)["error"]["code"])
print(r.headers)
