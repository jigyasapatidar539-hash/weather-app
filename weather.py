import requests
from config import API_KEY, BASE_URL

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        print(f"City not found: {city}")
        return

    print(f"""
Location  : {data['name']}, {data['sys']['country']}
Temp      : {data['main']['temp']}°C
Humidity  : {data['main']['humidity']}%
Condition : {data['weather'][0]['description']}
    """)

def main():
    while True:
        city = input("City name daalo (quit karne ke liye 'quit' likho): ")
        if city.lower() == "quit":
            break
        get_weather(city)

if __name__ == "__main__":
    main()