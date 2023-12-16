import requests
from country import Country
from newsdataapi import NewsDataApiClient

api = NewsDataApiClient(apikey='pub_34760291d1d85adc505aaa47d2a3fdb8cb2d1')

response = api.news_api(q="antisemitism OR antisemitic", country = "fr")

print(response)

# class News:

#     def __init__(self, country):
#         self.country = country

#     def get_keywords(self):
#         keyword_list = ['antisemitism, antisemitic']
#         if self.country.language:
#             translator= Translator(to_lang=self.country.language)
#             keyword.list.append(translator.translate('antisemitism'), translator.translate('antisemitic'))
#         return keyword_list

#     def get_data(self, url):
#         data = []
#         response = requests.get(url)
#         if response.status_code == 200:
#             data.append(response.json())

#     def save_data(self):
#         with open(dir_path + '/news.json', mode = 'w') as file:
#             json.dump(self.data, file)

#     def count_articles(self):
#         return len(self.data)