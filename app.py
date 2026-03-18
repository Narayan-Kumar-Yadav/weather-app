from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# OpenWeatherMap API base URL and key
API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5'

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route handles both GET (show form) and POST (fetch weather data for city).
    Fetches current weather and 5-day forecast, filters forecast to daily noon readings.
    """
    city = ''
    current_weather = None
    forecast = []
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        
        if not city:
            error = 'Please enter a city name.'
        else:
            try:
                # Fetch current weather
                current_params = {
                    'q': city,
                    'appid': API_KEY,
                    'units': 'metric'
                }
                current_response = requests.get(f"{BASE_URL}/weather", params=current_params)
                current_data = current_response.json()
                
                if current_response.status_code != 200:
                    error = current_data.get('message', 'City not found or API error.')
                else:
                    current_weather = {
                        'name': current_data['name'],
                        'temp': round(current_data['main']['temp']),
                        'description': current_data['weather'][0]['description'].capitalize(),
                        'humidity': current_data['main']['humidity'],
                        'icon': current_data['weather'][0]['icon']
                    }
                    
                    # Fetch 5-day forecast (every 3 hours)
                    forecast_params = {
                        'q': city,
                        'appid': API_KEY,
                        'units': 'metric'
                    }
                    forecast_response = requests.get(f"{BASE_URL}/forecast", params=forecast_params)
                    forecast_data = forecast_response.json()
                    
                    if forecast_response.status_code == 200:
                        # Filter to only noon (12:00:00) entries for each day, max 5 days
                        daily_forecast = []
                        seen_dates = set()
                        for item in forecast_data['list']:
                            dt_str = item['dt_txt']
                            if '12:00:00' in dt_str:
                                date = dt_str[:10]  # YYYY-MM-DD
                                if date not in seen_dates:
                                    seen_dates.add(date)
                                    daily_forecast.append({
                                        'date': datetime.strptime(date, '%Y-%m-%d').strftime('%A'),  # Day name e.g. Monday
                                        'temp': round(item['main']['temp']),
                                        'description': item['weather'][0]['description'].capitalize(),
                                        'icon': item['weather'][0]['icon']
                                    })
                                    if len(daily_forecast) == 5:
                                        break
                        forecast = daily_forecast
                    else:
                        error = forecast_data.get('message', 'Forecast unavailable.')
                        
            except requests.exceptions.RequestException:
                error = 'Network error. Please check your connection.'
            except Exception as e:
                error = f'An unexpected error occurred: {str(e)}'
    
    return render_template('index.html', 
                         city=city, 
                         current_weather=current_weather,
                         forecast=forecast,
                         error=error)

if __name__ == '__main__':
    app.run(debug=True)
