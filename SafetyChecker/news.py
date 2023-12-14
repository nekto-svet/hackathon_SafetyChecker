import requests
import os, json
from translate import Translator
from country import Country

dir_path = os.path.dirname(os.path.realpath(__file__))

class News:

    def __init__(self, country, eng=True):
        self.country = Country(country)
        self.eng = eng
        self.keywords = self.get_keywords()
        self.url = ''
        self.data = self.get_data(url)

    def get_keywords(self):
        keyword_list = ['antisemitism, antisemitic']
        if self.country.language:
            translator= Translator(to_lang=self.country.language)
            keyword.list.append(translator.translate('antisemitism'), translator.translate('antisemitic'))
        return keyword_list

    def get_data(self, url):
        data = []
        response = requests.get(url)
        if response.status_code == 200:
            data.append(response.json())

    def save_data(self):
        with open(dir_path + '/news.json', mode = 'w') as file:
            json.dump(self.data, file)

    def count_articles(self):
        return len(self.data)