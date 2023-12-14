import requests
import os, json

dir_path = os.path.dirname(os.path.realpath(__file__))

class NewsManager:

    def __init__(self, country, eng=True):
        self.country = country
        self.keywords = self.get_keywords()

    def get_keywords(self):
        pass

    def save_to_json(self):
        pass

    def count_articles(self):
        pass

url = ('https://newsapi.org/v2/top-headlines?country=fr&apiKey=e8965fac57ea48e4b4e04f9381f0aff2'
       'q=Apple&'
       'from=2023-12-14&'
       'sortBy=popularity&'
       'apiKey=e8965fac57ea48e4b4e04f9381f0aff2')

response = requests.get(url)

data = []

for i in range(1):
    response = requests.get(url)
    if response.status_code == 200:
        data.append(response.json())

with open(dir_path + '/news.json', mode = 'w') as file:
    json.dump(data, file)