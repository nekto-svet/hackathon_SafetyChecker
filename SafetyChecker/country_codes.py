import psycopg2
import os
from dotenv import load_dotenv
import pycountry

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv('db_name'),
    user=os.getenv('db_user'),
    password=os.getenv('db_password'),
    host=os.getenv('db_host'),
    port=os.getenv('db_port')
)

cur = conn.cursor()

cur.execute('ALTER TABLE travel_warning ADD country_code VARCHAR(2)')
cur.execute('ALTER TABLE travel_warning ADD language_code VARCHAR(2)')

cur.execute('SELECT country FROM travel_warning')
rows = cur.fetchall()

for row in rows:
    try:
        country = pycountry.countries.search_fuzzy(row[0])
        contry_code = country[0].alpha_2
    except:
        country_code = None
    try:
        language = pycountry.languages.get(alpha_2=contry_code)
        language_code = language.alpha_2
    except:
        language_code = None
    cur.execute('UPDATE travel_warning SET contry_code=%s, language_code=%s WHERE country=%s', (contry_code, language_code, row[0]))

conn.commit()

cur.close()
conn.close()