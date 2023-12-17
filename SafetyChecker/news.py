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

    def __init__(self, country):
        self.country = country

    def get_keywords(self):
        translator = Translator(to_lang=self.country.language)
        keyword_list = ['antisemitism', 'antisemitic']
        if self.country.language != 'en':
            keyword_list.append(translator.translate('antisemitism'))
            keyword_list.append(translator.translate('antisemitic'))
        return ' OR '.join(keyword_list)

    def save_data(self):
        data = News.api.news_api(q=self.get_keywords(), country = self.country.code)
        with open(dir_path + '/news.json', mode = 'w') as file:
            json.dump(data, file)

    def __call__(self):
        self.save_data()
        if self.country.language != 'en':
            translator = Translator(from_lang=self.country.language, to_lang='en')
        with open(dir_path + '/news.json', mode = 'r') as file:
            data = json.load(file)
            print(f"Total results for 'antisemitism' in the news: {data['totalResults']}")
            for i, article in enumerate(data['results'], start=1):
                if self.country.language != 'en':
                    print(f"#{i}: {translator.translate((article['title']))}\n{article['link']}\n{translator.translate((article['description'] if article['description'] else '-'))}\n")
                else:
                    print(f"#{i}: {(article['title'])}\n{article['link']}\n{(article['description'] if article['description'] else '-')}\n")