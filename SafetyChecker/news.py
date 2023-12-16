import json
import requests
import os
from dotenv import load_dotenv
from country import Country
from newsdataapi import NewsDataApiClient
from translate import Translator

dir_path = os.path.dirname(os.path.realpath(__file__))

load_dotenv()

class News:

    api = NewsDataApiClient(apikey=os.getenv('newsAPI'))

    def __init__(self, country, en=True):
        self.country = country
        self.en = en
        self.data = self.get_data()
        self.count = self.count_articles()

    def get_keywords(self):
        translator = Translator(to_lang=self.country.language)
        keyword_list = ['antisemitism', 'antisemitic']
        if self.country.language != 'en':
            keyword_list.append(translator.translate('antisemitism'))
            keyword_list.append(translator.translate('antisemitic'))
        return ' OR '.join(keyword_list)

    def get_data(self):
        return News.api.news_api(q=self.get_keywords(), country = self.country.code)

    def save_data(self):
        with open(dir_path + '/news.json', mode = 'w') as file:
            json.dump(self.data, file)

    def count_articles(self):
        return self.data['totalResults']

    def __call__(self):
        translator = Translator(from_lang=self.country.language, to_lang='en')
        print(f'Relevant news: {self.count}')
        for i, article in enumerate(self.data['results'], start=1):
            if self.en:
                print(f"#{i}: {translator.translate((article['title']))}")
            else:
                print(article['title'])
            print(f"Link: {article['link']}\n")