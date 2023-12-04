import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

def main():
    # Replace 'YOUR_API_KEY' with the API key you obtained from OpenWeather
    api_key = 'YOUR_API_KEY'

    # Get user input for the city
    city = input("Enter the name of a municipality: ")

    # Get weather data from OpenWeather API
    weather_data = get_weather(api_key, city)

    if weather_data:
        # Extract relevant information from the API response
        weather_description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']

        # Convert temperature from Kelvin to Celsius
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)

        # Print the weather information
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f} °C")
    else:
        print("Weather information not available.")

if __name__ == "__main__":
    main()
