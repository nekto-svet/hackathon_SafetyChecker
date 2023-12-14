import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Country:

    def __init__(self, name):
        self.name = name
        self.threat = self.get_data(f"SELECT threat_lvl, threat_lvl FROM travel_warning WHERE country LIKE '%{name}%'")
        self.details = self.get_data(f"SELECT details FROM travel_warning WHERE country LIKE '%{name}%'")
        self.rec = self.get_data(f"SELECT recommendation FROM travel_warning WHERE country LIKE '%{name}%'")

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