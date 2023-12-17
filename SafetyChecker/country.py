import psycopg2
import os
from dotenv import load_dotenv
import pycountry

load_dotenv()

class Country:

    def __init__(self, user_input):
        self.user_input = user_input
        self.code = self.get_code()
        self.name = self.get_data(f"SELECT country FROM travel_warning WHERE country_code = '{self.code}'")
        self.language = self.get_data(f"SELECT language_code FROM travel_warning WHERE country_code = '{self.code}'") or 'en'
        self.threat = self.get_data(f"SELECT threat_lvl FROM travel_warning WHERE country_code = '{self.code}'")
        self.details = self.get_data(f"SELECT details FROM travel_warning WHERE country_code = '{self.code}'")
        self.rec = self.get_data(f"SELECT recomendations FROM travel_warning WHERE country_code = '{self.code}'")

    def get_code(self):
        try:
            country = pycountry.countries.search_fuzzy(self.user_input)
            return country[0].alpha_2
        except LookupError:
            return None

    def get_data(self, query): 
        conn = psycopg2.connect(
            dbname=os.getenv('db_name'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            host=os.getenv('db_host'),
            port=os.getenv('db_port')
        )
        cur = conn.cursor()
        cur.execute(query)
        item = cur.fetchone()
        if item:
            data = item[0]
        else:
            data = None
        cur.close()
        conn.close()
        return data

    def __call__(self):
        print(f'''
Country: {self.name}
Threat level: {self.threat}
Details: {self.details}
Recommendation: {self.rec}
''')

    def threat_lvl(self):
        return max(map(int, self.threat.split('/')))

    def compare_threat(self, other):
        if self.threat_lvl() < other.threat_lvl():
            return(f'{self.name} is less dangerous than {other.name}')
        elif self.threat_lvl() > other.threat_lvl():
            return(f'{self.name} is more dangerous than {other.name}')
        else:
            return(f'{self.name} and {other.name} are equally dangerous')