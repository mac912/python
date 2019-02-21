import requests
r = requests.get("https://www.google.com")
print("status:", r.status_code)
