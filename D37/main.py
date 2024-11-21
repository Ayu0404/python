import os
from dotenv import load_dotenv
import requests
import datetime

load_dotenv()

now = datetime.datetime.now()

createUserEndpoint = "https://pixe.la/v1/users"
graphEndpoint = f"{createUserEndpoint}/{os.getenv('PIXELA_USERNAME')}/graphs"
pixelEndpoint = f"{graphEndpoint}/{os.getenv('PIXELA_GRAPHID')}"
updatePixel = f"{pixelEndpoint}/"  # /<yyyyMMdd>


# Create a user
params = {
    "token": os.getenv('PIXELA_TOKEN'),
    "username": os.getenv('PIXELA_USERNAME'),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=createUserEndpoint, json=params)
# print(response.json())

# Create a graph for username
headers = {
    "X-USER-TOKEN": os.getenv('PIXELA_TOKEN')
}
body = {
    "id": os.getenv('PIXELA_GRAPHID'),
    "name": "Daily Impromptu Speaking",
    "unit": "days",
    "type": "int",
    "color": "shibafu",

}

# res = requests.post(url=graphEndpoint, headers=headers, json=body)
# print(res.json())


# Enter a pixel
pixelBody = {
    "date": now.date().strftime("%Y%m%d"),
    "quantity": "1",
    "optionalData": ""
}
# Post Request
# pixelRes = requests.post(url=pixelEndpoint, headers=headers, json=pixelBody)
# print(pixelRes.json())

# Put Request
date = now.date().strftime("%Y%m%d")
updatePixel += date
updateData = {
    "quantity": "15",
}
# update = requests.put(url=updatePixel, headers=headers, json=updateData)
# print(update.json())


# Delete Pixel
delURL = updatePixel+now.date().strftime("%Y%m%d")
delPixel = requests.delete(url=updatePixel, headers=headers)
print(delPixel.json())
