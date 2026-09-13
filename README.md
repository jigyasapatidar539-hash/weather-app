# Weather App (Python + OpenWeatherMap API)

A simple command-line weather application that fetches real-time weather data for any city using the OpenWeatherMap API.

## Features

- Get current weather for any city (entered by the user)
- Displays:
  - Location (city + country)
  - Temperature (°C)
  - Humidity (%)
  - Weather condition (e.g., clear sky, rain, clouds)
- Handles invalid/city-not-found errors gracefully
- Runs in a loop — keep checking multiple cities until you type `quit`

## Tech Stack

- **Language:** Python
- **Library:** `requests`
- **API:** [OpenWeatherMap](https://openweathermap.org/api)

## Project Structure

```
weather-app/
├── config.py       # Stores API key and base URL
└── weather.py       # Main script — fetches and displays weather data
```

## Setup

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)

2. Add your API key in `config.py`:
   ```python
   API_KEY = "your_api_key_here"
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
   ```

3. Install dependencies
   ```bash
   pip install requests
   ```

4. Run the app
   ```bash
   python weather.py
   ```

## Usage

```
City name daalo (quit karne ke liye 'quit' likho): Indore

Location  : Indore, IN
Temp      : 29°C
Humidity  : 58%
Condition : clear sky
```

Type `quit` anytime to exit the loop.

## Author

**Jigyasa Patidar**

## License

This project is open source and available for educational purposes.
