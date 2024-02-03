# # from flask import Blueprint, render_template, request, Response
# # cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]
# # views = Blueprint('views', __name__)
# # @views.route('/')

# # def home():
# #     if request.method == 'POST':
# #         selected_city = request.form.get('city')
# #         return f'Selected city: {selected_city}'
# #     return render_template("base.html", cities=cities)


# from website import app, api
# from flask import render_template, request, Response, redirect, url_for
# import requests
# # cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]
# # views = Blueprint('views', __name__)
# # @views.route('/')

# # def home():
# #     if request.method == 'POST':
# #         selected_city = request.form.get('city')
# #         return f'Selected city: {selected_city}'
# #     return render_template("base.html", cities=cities)

# @app.route("/")
# def get_weather_data():
#     API_KEY = '4c1d64bec949b1fedecc27ffe4970435'
#     BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#     city = request.form['city_name']
#     country = request.form['country']

#     params = {'q':city, 'appid':API_KEY}
#     response = requests.get(BASE_URL, params = params)
#     weather_data = response.json()

#     print(weather_data)
#     return render_template('base.html')

from flask import Blueprint, render_template, request
import requests
cities = ["New York", "London", "Tokyo", "Paris", "Berlin"]
views = Blueprint('views', __name__)

API_KEY = '4c1d64bec949b1fedecc27ffe4970435'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@views.route('/', methods=['GET','POST'])
def get_weather_data():
    if request.method == 'POST':
        city = request.form['city']

        params = {'q': city, 'appid': API_KEY}
        response = requests.get(BASE_URL, params=params)
        weather_data = response.json()
        print(weather_data)
        if response.status_code == 200:
            # Extract relevant weather information
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']

            return render_template('weather_result.html', city=city, temperature=temperature, description=description)
        else:
            error_message = f"Error: {weather_data['message']}"
            return render_template('error.html', error_message=error_message)

    return render_template('weather_form.html')


# def home():
#     if request.method == 'POST':
#         selected_city = request.form.get('city')
#         return f'Selected city: {selected_city}'
#     return render_template("base.html", cities=cities)