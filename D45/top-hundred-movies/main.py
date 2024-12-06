import requests
from bs4 import BeautifulSoup
endpoint = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=endpoint)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
headings = soup.select('h2>strong')

movies = [{
    'ranking': int(heading.getText().split(')')[0]),
    'movie': heading.getText().split(')')[1]+')'
} for heading in headings]

with open('D45/top-hundred-movies/movies.txt', 'w') as file:
    for movie in reversed(movies):
        file.write(f'{movie['ranking']}. {movie['movie']}\n')
