import requests
import sys
import os


def obte_ciutat_i_temperatura():
    # Demanar el nom de la ciutat
    ciutat = input("Introdueix el nom de la ciutat: ")
    
    # Demanar la temperatura que l'usuari creu que hi ha
    temperatura = float(input(f"Quina temperatura creus que hi ha a {ciutat}? "))

    # Mostra el resultat
    print(f"A {ciutat}, creus que la temperatura és de {temperatura} graus.")

    return ciutat, temperatura
    

def obtenir_temperatura(ciutat):
    # Introdueix aquí la teva clau API d'OpenWeatherMap
    api_key = os.getenv('API_KEY_OPENWEATHERMAP')
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": ciutat,
        "appid": api_key,
        "units": "metric",  # Per obtenir la temperatura en graus Celsius
    }
    
    # Realitzar la sol·licitud GET
    resposta = requests.get(base_url, params=params)
    
    # Comprovar si la sol·licitud ha estat exitosa
    if resposta.status_code == 200:
        dades = resposta.json()
        temperatura = dades["main"]["temp"]
        print(f"La temperatura actual a {ciutat} és de {temperatura}°C.")
    else:
        print(f"No s'ha pogut obtenir la temperatura per a {ciutat}. Comprova que el nom de la ciutat sigui correcte.")
        sys.exit(1)

    return temperatura

def compara_temperatures(temperatura_real, temperatura_suposada, tolerancia=1):
    # Calcula la diferència entre la temperatura real i la suposada
    diferència = abs(temperatura_real - temperatura_suposada)
    
    # Comprova si la diferència està dins de la tolerància
    if diferència <= tolerancia:
        print(f"La temperatura suposada ({temperatura_suposada}°C) és CORRECTE dins d'una tolerància de ±{tolerancia}°C.")
    else:
        print(f"La temperatura suposada ({temperatura_suposada}°C) no és correcte.")


def main():
    while True:
        ciutat, temperatura = obte_ciutat_i_temperatura()
        temperatura_real = obtenir_temperatura(ciutat)
        compara_temperatures(temperatura_real, temperatura)

if __name__ == "__main__":
    main()
