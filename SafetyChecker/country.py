import psycopg2
import os
from dotenv import load_dotenv
import pycountry

load_dotenv()

class Country:
    '''Country information based on the sql table

    Parameters
    user_input (string): name of the country as entered by user

    Methods
    get_code: returns the ISO 3166-1 alpha-2 country code from user_input
    get_data: connects to the database to retrieve data
    __call__: prints formatted info about the country
    threat_lvl: returns an int value of the threat level
    compare_threat: compares the threat levels between two Country instances
    ''' 

    def __init__(self, user_input:str):
        self.user_input = user_input
        self.code = self.get_code()
        self.data = self.get_data(f"SELECT country, language_code, threat_lvl, details, recomendations FROM travel_warning WHERE country_code = '{self.code}'")
        self.name = self.data[0]
        self.language = self.data[1]
        self.threat = self.data[2]
        self.details = self.data[3]
        self.rec = self.data[4]

    def get_code(self):
        try:
            country = pycountry.countries.search_fuzzy(self.user_input)
            return country[0].alpha_2
        except LookupError:
            return None

    def get_data(self, query:str): 
        conn = psycopg2.connect(
            dbname=os.getenv('db_name'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            host=os.getenv('db_host'),
            port=os.getenv('db_port')
        )
        cur = conn.cursor()
        cur.execute(query)
        item = cur.fetchall()
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
        if len(self.threat) > 2: 
            # returns average threat for countries with mixed threat level
            threat_lvls = list(map(int, self.threat.split('/')))
            return ((threat_lvls[0] + threat_lvls[1])//2)
        else:
            return int(self.threat)

    def compare_threat(self, other):
        if self.threat_lvl() < other.threat_lvl():
            return(f'{self.name} is less dangerous than {other.name}')
        elif self.threat_lvl() > other.threat_lvl():
            return(f'{self.name} is more dangerous than {other.name}')
        else:
            return(f'{self.name} and {other.name} are equally dangerous')