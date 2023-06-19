# escreva um código python que liste os primeiros 150 pokemons

import requests
import json

def main():
    url = "https://pokeapi.co/api/v2/pokemon?limit=150"
    response = requests.get(url)
    pokemons = json.loads(response.text)
    for pokemon in pokemons['results']:
        print(pokemon['name'])

if __name__ == "__main__":
    main()
