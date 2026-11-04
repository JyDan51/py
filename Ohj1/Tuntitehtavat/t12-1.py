import requests
import json

pk = input("Give pocemon name: ")

pg = f"https://pokeapi.co/api/v2/pokemon/{pk}/"

try:
    vastaus = requests.get (pg)
    if vastaus.status_code == 200:
        vastaus = vastaus.json()
        print ("Pokem type :", vastaus["types"][0]["type"]["name"])
    else:
        print ("Pokemon not find")
except requests.exceptions.RequestException as e:

    print ("Hakua ei voitu suorittaa.")