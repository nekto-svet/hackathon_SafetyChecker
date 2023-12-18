from flask import Flask, render_template, request
from country import Country
from news import News

# This is a main logic of app, that connect html interface with python code and all functions via Flask

app = Flask(__name__)

# routes for links in HTML files
@app.route('/')
def index():
    return render_template('index.html')

def one_country():
    return render_template('templates/one_country.html')

def compare_countries():
    return render_template('templates/compare_countries')

# The first function, that takes input from the page 'one_country' and returns results of the objects 'Country' and 'News' to the page 'result'
@app.route('/result', methods=['GET', 'POST'])
def one_country():
    if request.method == 'POST':
        country_name = request.form['country_name']
        curr_country = country_name.strip().lower().capitalize()
        try:
            country = Country(curr_country)
            news = News(country)
            country_info = country.info()
            text_news = news.get_text().split('#')
            result1 = f"INFO ABOUT COUNTRY:{country_info}"
            try:
                result2 = f"NEWS:{text_news[0]}"
            except:
                result2 = ''
            try:
                result3 = f"NEWS:{text_news[1]}"
            except:
                result3 = ''
            try:
                result4 = f"NEWS:{text_news[2]}"
            except:
                result4 = ''
            try:
                result5 = f"NEWS:{text_news[3]}"
            except:
                result5 = ''
        except:
            result1 = 'There is no country with this name, try again'
            result2 = ''
            result3 = ''
            result4 = ''
            result5 = ''
        return render_template('result.html', result1=result1, result2=result2, result3=result3, result4=result4, result5=result5)
    return render_template('one_country.html')

# The second function, that takes input from the page 'compare_countries' and returns results of method 'compare_threat' of the objects 'Country' to the page 'result1'
@app.route('/result2', methods=['GET', 'POST'])
def compare_countries():
    if request.method == 'POST':
        countries = request.form['countries']
        try:
            country_names = countries.split(',')
            country_one = country_names[0].strip().lower().capitalize()
            country_two = country_names[1].strip().lower().capitalize()
            country_obj1 = Country(country_one)
            country_obj2 = Country(country_two)
            compare = country_obj1.compare_threat(country_obj2)
            result = f'{compare}'
        except:
            result = 'There is no countries with this names, try again'
        return render_template('result2.html', result=result)
    return render_template('compare_countries.html')


if __name__ == '__main__':
    app.run(debug=True)