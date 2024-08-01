# 1.importeer van benodigde modules
import requests
import sys

# 2.Definieer API-eindpunten en sleutels
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_api_url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "b360f92fbe23a598b81743c9bf5b78e7"

# 3.Definieer functie om weergegevens op te halen
def get_current_weather(city):
     try:
            url = f"{weather_api_url}weather?q={city}&appid={api_key}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
     except requests.RequestException as e:
            print(f"Error fetching current weather data: {e}")
     return None
def get_forecast(city):
    try:
            url = f"{forecast_api_url}forecast?q={city}&appid={api_key}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
    except requests.RequestException as e:
            print(f"Error fetching forecast data: {e}")
            return None

# functies
# Implement functie 1 temperatuur celcius
def unique_functionality_1(data):

    if data:
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        print(f"Current temperature: {temp_celsius:.2f}°C")

# Implement functie 2 weer omstandigheden
def unique_functionality_2(data):

    if data:
        description = data['weather'][0]['description']
        print(f"Weather description: {description}")

# Implement functie 3 wind snelheid
def unique_functionality_3(data):

    if data:
        wind_speed = data['wind']['speed']
        print(f"Wind speed: {wind_speed} m/s")

# 5.Definieer menuopties
def display_menu():
    print("Weer App Menu")
    print("1. Huidige weer bekijken")
    print("2. Weersvoorspelling bekijken")
    print("3. Temperatuur in Celsius weergeven")
    print("4. Afsluiten")
    choice = input("Maak een keuze (1-4):")
    return choice

# 6.Definieer hoofdprogramma
def main():
    while True:
        try:
            choice = display_menu()
            if choice == "1":
                city = input("Voer de stad in: ")
                weather_data = get_current_weather(city)
                unique_functionality_1(weather_data)
            elif choice == "2":
                city = input("Voer de stad in: ")
                forecast_data = get_forecast(city)
                unique_functionality_2(forecast_data)
            elif choice == "3":
                city = input("Voer de stad in: ")
                weather_data = get_current_weather(city)
                unique_functionality_1(weather_data)
            elif choice == "4":
                print("Applicatie afsluiten")
                sys.exit()
            else:
                print("Ongeldige keuze, probeer opnieuw.")
        except Exception as e:
            print(f"Er is een fout opgetreden: {e}")


# 7.Implementeren van foutafhandeling

def main():
    while True:
        try:
            choice = display_menu()
            if choice == "1":
                city = input("Voer de stad in: ")
                weather_data = get_current_weather(city)
                unique_functionality_1(weather_data)
            elif choice == "2":
                city = input("Voer de stad in: ")
                forecast_data = get_forecast(city)
                unique_functionality_2(forecast_data)
            elif choice == "3":
                city = input("Voer de stad in: ")
                weather_data = get_current_weather(city)
                unique_functionality_1(weather_data)
            elif choice == "4":
                print("Applicatie afsluiten.")
                sys.exit()
            else:
                print("Ongeldige keuze, probeer opnieuw.")
        except Exception as e:
            print(f"Er is een fout opgetreden: {e}")


if __name__ == "__main__":
    main()