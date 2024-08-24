import requests

def get_weather(city_name):
    weather_url = f"https://wttr.in/{city_name}?format=j1"
    response = requests.get(weather_url)
    weather_data = response.json()

    if 'current_condition' in weather_data:
        current_weather = weather_data['current_condition'][0]
        temperature = current_weather['temp_C']
        weather_desc = current_weather['weatherDesc'][0]['value']
        return f"Temperatura: {temperature}°C\nCondição: {weather_desc}"
    else:
        return "Não foi possível obter o clima."

# Exemplo de uso
cidade = "Caieiras"
print(get_weather(cidade))
