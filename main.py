import requests
import sys

# 2. Definieer API-eindpunten en sleutels
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_api_url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "b360f92fbe23a598b81743c9bf5b78e7"


# 3. Definieer functie om weergegevens op te halen
def get_current_weather(city):
    try:
        url = f"{weather_api_url}?q={city}&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return None


def get_forecast(city):
    try:
        url = f"{forecast_api_url}?q={city}&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return None


# Implement functie 1 temperatuur celcius
def display_temperature(data):
    if data:
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        print(f"Current temperature: {temp_celsius:.2f}°C")


# Implement functie 2 weer omstandigheden
def display_weather_description(data):
    if data:
        description = data['weather'][0]['description']
        print(f"Weather description: {description}")


# Implement functie 3 wind snelheid
def display_wind_speed(data):
    if data:
        wind_speed = data['wind']['speed']
        print(f"Wind speed: {wind_speed} m/s")


# 5. Definieer menuopties
def display_menu():
    print("Weer App Menu")
    print("1. Huidige weer bekijken")
    print("2. Weersvoorspelling bekijken")
    print("3. Wind snelheid")
    print("4. Afsluiten")
    choice = input("Maak een keuze (1-4):")
    return choice


# 6. Definieer hoofdprogramma
def main():
    while True:
        try:
            choice = display_menu()
            if choice == "1":
                city = input("Voer de stad in: ")
                weather_data = get_current_weather(city)
                if weather_data:
                    display_temperature(weather_data)
                    display_weather_description(weather_data)
                    display_wind_speed(weather_data)
                else:
                    print("Kon de huidige weergegevens niet ophalen, probeer opnieuw")
            elif choice == "2":
                city = input("Voer de stad in: ")
                forecast_data = get_forecast(city)
                if forecast_data:
                    print("Weersvoorspelling voor de komende dagen:")
                    for forecast in forecast_data['list'][:5]:  # Weergeven van de eerste 5 voorspellingen
                        display_temperature(forecast)
                        display_weather_description(forecast)
                else:
                    print("Kon de huidige weergegevens niet ophalen, probeer opnieuw")
            elif choice == "3":
                city = input("Voer de stad in: ")
                weather_data = get_current_weather(city)
                if weather_data:
                    display_wind_speed(weather_data)
                else:
                    print("Kon de huidige weergegevens niet ophalen, probeer opnieuw")
            elif choice == "4":
                print("Applicatie afsluiten.")
                sys.exit()
            else:
                print("Ongeldige keuze, probeer opnieuw.")
        except Exception as e:
            print(f"Er is een fout opgetreden: {e}")


if __name__ == "__main__":
    main()
