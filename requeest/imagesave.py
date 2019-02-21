# this script is used to save the image from a given link
import requests
from io import BytesIO
from PIL import Image
r = requests.get("https://wallpapercave.com/w/wp3998474.jpg")
print("status", r.status_code)
image = Image.open(BytesIO(r.content))
path = "./image1."+image.format
print(image.size, image.format, image.mode)
try:
    image.save(path, image.format)
except IOError:
    print("Can not save image")
