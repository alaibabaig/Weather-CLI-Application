import requests

# Replace with your OpenWeatherMap API key
API_KEY = "5e7a2b5f18f07ef07a4e471059005398"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # For temperature in Celsius
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Condition": data["weather"][0]["description"].capitalize()
        }
        return weather
    elif response.status_code == 404:
        return "City not found. Please check the name and try again."
    else:
        return f"Error: Unable to fetch data (Status Code: {response.status_code})"

def main():
    print("📍 Welcome to the CLI Weather App 🌤️")
    city = input("Enter the city name: ").strip()

    result = get_weather(city)

    print("\n==========================")
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)
    print("==========================")

if __name__ == "__main__":
    main()


