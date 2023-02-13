from pokemon_rest_app.models import Pokemons, Evolutions
import requests

# VARIABLES
# Evolution-Chain Pokemon API URL
api_url_evolution = "https://pokeapi.co/api/v2/evolution-chain/"
# Pokemon Information API URL
api_url_pokemon = "https://pokeapi.co/api/v2/pokemon/"

# Pokemons with two options on the second evolution
special_chain_3 = ["442", "213", "188", "144", "33", "186", "58"]
# Pokemons with two options on the third evolution
special_chain_4 = ["413", "18", "140", "26"]
# Tyrogue: three options for the second evolution
unique_structure_chain_4 = ["47"]
# Wurmple: two options for the second evolution and then one option for each of the third evolutions
unique_structure_chain_5 = ["135"]
# Eevee: eight options for the second evolution
unique_structure_chain_9 = ["67"]

# Current Chain IDs
max_chain_id = 477


def get_evolution_chain(evolution_chain_id):
    pokemon_chain_url = api_url_evolution + evolution_chain_id
    response = requests.get(pokemon_chain_url)

    try:
        data = response.json()
        data_evolutions_counter = str(data).count("evolves_to")
        evolution_dictionary = {}
        evolution_list = []

        if evolution_chain_id in special_chain_3:

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][1]["species"]["name"]

        elif evolution_chain_id in special_chain_4:

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["fourth_pokemon"] = data["chain"]["evolves_to"][0]["evolves_to"][1]["species"]["name"]

        elif evolution_chain_id in unique_structure_chain_4:

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][1]["species"]["name"]
            evolution_dictionary["fourth_pokemon"] = data["chain"]["evolves_to"][2]["species"]["name"]

        elif evolution_chain_id in unique_structure_chain_5:

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][1]["species"]["name"]
            evolution_dictionary["fourth_pokemon"] = data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["fifth_pokemon"] = data["chain"]["evolves_to"][1]["evolves_to"][0]["species"]["name"]

        elif evolution_chain_id in unique_structure_chain_9:

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][1]["species"]["name"]
            evolution_dictionary["fourth_pokemon"] = data["chain"]["evolves_to"][2]["species"]["name"]
            evolution_dictionary["fifth_pokemon"] = data["chain"]["evolves_to"][3]["species"]["name"]
            evolution_dictionary["sixth_pokemon"] = data["chain"]["evolves_to"][4]["species"]["name"]
            evolution_dictionary["seventh_pokemon"] = data["chain"]["evolves_to"][5]["species"]["name"]
            evolution_dictionary["eighth_pokemon"] = data["chain"]["evolves_to"][6]["species"]["name"]
            evolution_dictionary["ninth_pokemon"] = data["chain"]["evolves_to"][7]["species"]["name"]

        elif data_evolutions_counter == 1:

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]

        elif data_evolutions_counter == 2:

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]

        elif data_evolutions_counter == 3:

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]

        for x in evolution_dictionary.values():
            evolution_list.append(x)

        chain_id = data["id"]

        print(evolution_dictionary)
        print(pokemon_chain_url)

        return evolution_list, chain_id

    except ValueError:
        print("Invalid Evolution Chain Number: Enter a Number Between 1-477")
        print("Please note that NOT all pokemon evolution chains are available")
        print(pokemon_chain_url)


def get_and_save_pokemon_information(pokemon_evolution_list, chain_id):

    for pokemon in pokemon_evolution_list:
        pokemon_url = api_url_pokemon + pokemon
        response = requests.get(pokemon_url)
        data = response.json()

        poke = Pokemons()

        poke.mon_id = data["id"]
        poke.evolution_chain_id = chain_id
        poke.name = data["name"]
        poke.first_type = data["types"][0]["type"]["name"]

        try:
            poke.second_type = data["types"][1]["type"]["name"]
        except IndexError:
            poke.second_type = ""

        poke.height = data["height"]
        poke.weight = data["weight"]
        poke.hp = data["stats"][0]["base_stat"]
        poke.attack = data["stats"][1]["base_stat"]
        poke.defense = data["stats"][2]["base_stat"]
        poke.special_attack = data["stats"][3]["base_stat"]
        poke.special_defense = data["stats"][4]["base_stat"]
        poke.speed = data["stats"][5]["base_stat"]
        poke.evolutions_list = pokemon_evolution_list

        poke.save()