import random
import requests

pokemon_list = ["pikachu", "charizard", "bulbasaur", "squirtle", "gengar"]

target = random.choice(pokemon_list)

url = "https://pokeapi.co/api/v2/pokemon/" + target
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    name = data["name"]
    height = data["height"]
    weight = data["weight"]
    
    abilities = []
    for item in data["abilities"]:
        ability_name = item["ability"]["name"]
        abilities.append(ability_name)
    
    print("=== WHOS THAT POKEMON ===")
    print("Height:", height)
    print("Weight:", weight)
    print("Abilities:", abilities)
    print("=========================")
    
    guessed = False
    for attempt in range(1, 4):
        guess = input(f"Attempt {attempt}/3 - Guess the pokemon: ").lower().strip()
        
        if guess == name:
            print("It's", name)
            guessed = True
            break
        else:
            print("Wrong guess. You still have some pokeballs.")
            
    if not guessed:
        print("Game Over! Team Rocket captured", name)

else:
    print("Error getting data from API. Code:", response.status_code)