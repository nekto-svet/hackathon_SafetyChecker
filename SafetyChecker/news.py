import json
import os
from dotenv import load_dotenv
from country import Country
from newsdataapi import NewsDataApiClient
from translate import Translator

dir_path = os.path.dirname(os.path.realpath(__file__))

load_dotenv()

class News:
    '''News about antisemitism from a specified country
    Needs newsAPI key from .env

    Parameters
    country (object): instance of the Country class

    Methods
    get_keywords: returns a list of keywords for the api search, adding translations to the language of the country
    save_data: saves api data to json
    __repr__: returns formatted string from json, translation to English if necessary 
    ''' 

    api = NewsDataApiClient(apikey=os.getenv('newsAPI'))

    def __init__(self, country:object):
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

    def get_text(self):
        try:
            self.save_data()
        except:
           return 'News unavailable'
        else:
            text = ''
            if self.country.language != 'en':
                translator = Translator(from_lang=self.country.language, to_lang='en')
            with open(dir_path + '/news.json', mode = 'r') as file:
                data = json.load(file)
                text += f"Total results for 'antisemitism' in the news: {data['totalResults']}\n"
                for i, article in enumerate(data['results'], start=1):
                    if self.country.language != 'en':
                        text += f"#{i}: {translator.translate((article['title']))}\n{article['link']}\n{translator.translate((article['description'] if article['description'] else '-'))}\n\n"
                    else:
                        text += f"#{i}: {(article['title'])}\n{article['link']}\n{(article['description'] if article['description'] else '-')}\n\n"
            return text