import pyowm

# Replace with your own OpenWeather API key
API_KEY = 'YOUR_API_KEY'
owm = pyowm.OWM(API_KEY)

def get_weather(city):
    observation = owm.weather_manager().weather_at_place(city)
    weather = observation.weather
    return weather.status, weather.temperature('celsius')['temp']

if __name__ == "__main__":
    city = input("Enter the city name: ")
    status, temperature = get_weather(city)
    print(f"Weather in {city}: {status}, Temperature: {temperature}°C")
