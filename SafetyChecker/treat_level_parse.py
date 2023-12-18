from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psycopg2
import os
from dotenv import load_dotenv


# This is the functions that allow to take information from the certain page of gov.il and to write in to a Data Base


# Connection
def get_connect():
    load_dotenv()

    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASS')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    connection = psycopg2.connect(
        dbname = db_name,
        user = db_user,
        password = db_password,
        host = db_host,
        port = db_port
        )

    return connection
    

# Parce the site via Selenium, because the site was wrote with Angular
# for this function you need relevant browser driver on your computer
def parser():
    driver = webdriver.Chrome()
    list_countries = []
    
    for p in range (0, 200, 10):
        try:
            url = f"https://www.gov.il/en/departments/dynamiccollectors/travel-warnings-nsc?skip={p}"
            driver.get(url)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@ng-app]')))
        except:
            pass
        for i in range (1,11):
            try:
                xpath = f'//*[@id="content"]/div[2]/div[2]/div[3]/ul/li[{i}]/div/div/div[1]/div[2]'
                element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                text_content = element.text
                list_countries.append(text_content)
                # print(text_content)
            except:
                pass
    
    driver.quit()

    return list_countries



#  This function takes results of the first two functions and writes it to DB
def insert_data():
    connection = get_connect()
    cur = connection.cursor()

    list_countries = parser()

    for country in list_countries:
        current_country = country.split('\n')

        name = current_country[1]
        threat_level = current_country[3]
        recomendations = current_country[5]
        area_under_threat = current_country[7]
        details = current_country[9]

        insert_query = 'INSERT INTO travel_warning (country, threat_lvl, recomendations, area_under_threat, details) VALUES (%s, %s, %s, %s, %s)'
        data_to_insert = (name, threat_level, recomendations, area_under_threat, details)
        cur.execute (insert_query, data_to_insert)
        connection.commit()

    cur.close()
    connection.close()

if __name__ == "__main__":
    insert_data()
    

