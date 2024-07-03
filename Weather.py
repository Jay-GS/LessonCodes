import tkinter as tk 
from tkinter import messagebox 
import requests 
from datetime import datetime, timedelta 
import pytz 
# Function to get weather data from OpenWeatherMap 
def get_weather(city):
    api_key = "dc6544895aca68d90c1e600d51bef4f0" # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(complete_url)
    return response.json()
# Function to get local time for the city
def get_local_time(timezone_offset):
    utc_time = datetime.utcnow()
    local_time = utc_time + timedelta(seconds=timezone_offset)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')
    # Function to display weather
def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    if weather_data['cod'] == '404':
        messagebox.showerror("Error", f"City {city} not found!")
    else:
        city_name = weather_data['name']
        temp = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        timezone_offset = weather_data['timezone']
        local_time = get_local_time(timezone_offset)
        result = f"City: {city_name}\nTemperature: {temp}°C\nWeather: {weather_desc}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nLocal Time: {local_time}"
        weather_result_label.config(text=result)
        # Setting up the GUI
app = tk.Tk() 
app.title("Live Weather Update") 
app.geometry("400x400") 
city_label = tk.Label(app, text="Enter city name:", font=("bold", 14))
city_label.pack(pady=10) 
city_entry = tk.Entry(app, width=25, font=("bold", 14))
city_entry.pack(pady=10) 
get_weather_button = tk.Button(app, text="Get Weather", command=show_weather, font=("bold", 14)) 
get_weather_button.pack(pady=10) 
weather_result_label = tk.Label(app, text="", font=("bold", 14))
weather_result_label.pack(pady=20) 
app.mainloop()
