from flask import Flask, render_template, request
from country import Country
from news import News

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/result', methods=['POST'])
# def result():
#     if request.method == 'POST':
#         word = request.form['word']
#         return render_template('result.html', word=word)

# if __name__ == '__main__':
#     app.run(debug=True)




@app.route('/')
def index():
    return render_template('index.html')

def one_country():
    return render_template('templates/one_country.html')

def compare_countries():
    return render_template('templates/compare_countries')

@app.route('/result', methods=['GET', 'POST'])
def one_country():
    if request.method == 'POST':
        country_name = request.form['country_name']
        curr_country = country_name.strip().lower().capitalize()
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
        return render_template('result.html', result1=result1, result2=result2, result3=result3, result4=result4, result5=result5)
    return render_template('one_country.html')

@app.route('/result2', methods=['GET', 'POST'])
def compare_countries():
    if request.method == 'POST':
        countries = request.form['countries']
        country_names = countries.split(',')
        country_one = country_names[0].strip().lower().capitalize()
        country_two = country_names[1].strip().lower().capitalize()
        country_obj1 = Country(country_one)
        country_obj2 = Country(country_two)
        compare = country_obj1.compare_threat(country_obj2)
        result = f'{compare}'
        return render_template('result2.html', result=result)
    return render_template('compare_countries.html')


if __name__ == '__main__':
    app.run(debug=True)