import requests
from bs4 import BeautifulSoup

endpoint = "https://news.ycombinator.com/newest"
response = requests.get(url=endpoint)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
spans = soup.findAll('span', class_='titleline')
data = []

for span in spans:
    anchor = span.find('a', href=True)
    title = anchor.getText()
    link = anchor['href']
    data.append({
        "title": title,
        "link": link,
    })

points = soup.findAll('span', class_='score')
for i in range(0, len(points)):
    data[i]['points'] = int(points[i].getText().split()[0])

maxPoint = -99
maxPoints = []
for item in data:
    if item['points'] > maxPoint:
        maxPoint = item['points']
        maxPoints.clear()
    if maxPoint == item['points']:
        maxPoints.append(item)

print(maxPoints)
