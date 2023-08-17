# Simple weather app to understand how API's work
import requests

API_KEY = "f8b0f693c72145defce746a5c2c077d9"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    temperature_f = round((data["main"]["temp"] - 273.15) * 9/5 + 32, 2)
    
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} celsius")
    print(f"Temperature: {temperature_f} fahrenheit")

else:
    print("An error occurred.")