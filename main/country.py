import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Country:

    def __init__(self, name):
        self.name = name
        self.threat_lvl = get_data(f"SELECT threat_lvl FROM travel_warning WHERE country = '{self.name}'")
        self.details = get_data(f"SELECT details FROM travel_warning WHERE country = '{self.name}'")
        self.rec = get_data(f"SELECT recommendation FROM travel_warning WHERE country = '{self.name}'")

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
        if items:
            data = items[0]
        else:
            data = None
        cur.close()
        conn.close()
        return data


france = Country('France')

print(france.details)