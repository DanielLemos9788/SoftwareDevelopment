import requests
import sqlite3

#VARIABLES
##Evolution-Chain Pokemon API URL
api_url_evolution = "https://pokeapi.co/api/v2/evolution-chain/"
##Pokemon Information API URL
api_url_pokemon = "https://pokeapi.co/api/v2/pokemon/"

##Pokemons with two options on the second evolution
special_chain_3 = ["442", "213", "188", "144", "33", "186", "58"]
##Pokemons with two options on the third evolution
special_chain_4 = ["413", "18", "140", "26"]
##Tyrogue: three options for the second evolution
unique_structure_chain_4 = ["47"]
##Wurmple: two options for the second evolution and then one option for each of the third evolutions
unique_structure_chain_5 = ["135"]
##Eevee: eight options for the second evolution
unique_structure_chain_9 = ["67"]

##Evolution Chain Unique Identifier
evolution_chain_id = input("What Pokemon Evolution Chain You Wanna Fetch (Enter a Number Between 1-477)?: ")

class Pokemon():
    def __init__(self, mon_id, evolution_chain_id, name, first_type, second_type, height, weight,
                 hp, attack, defense, special_attack, special_defense, speed, evolutions_list):

        self.mon_id = mon_id
        self.evolution_chain_id = evolution_chain_id
        self.name = name
        self.first_type = first_type
        self.second_type = second_type
        self.height = height
        self.weight = weight
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.evolutions_list = evolutions_list
        self.connection = sqlite3.connect("pokemon_data_base.db")
        self.cursor = self.connection.cursor()

    def insert_pokemon_info(self, mon_id):
        self.cursor.execute("""
                        SELECT * FROM pokemon_information
                        WHERE mon_id = {}
                        """.format(mon_id))

        results = self.cursor.fetchone()
        print(results)

        if results == None:
            self.cursor.execute("""
                                INSERT INTO pokemon_information VALUES
                                ({}, {}, "{}", "{}", "{}", {}, {}, {}, {}, {}, {}, {}, {}, "{}")
                                """.format(self.mon_id, self.evolution_chain_id, self.name,
                                           self.first_type, self.second_type, self.height,
                                           self.weight, self.hp, self.attack, self.defense,
                                           self.special_attack, self.special_defense, self.speed,
                                           self.evolutions_list))
            self.connection.commit()
        else:
            print(f"Pokemon {self.name} Already Exists on Data Base")
            pass




    def load_pokemon_info(self, mon_id):
        self.cursor.execute("""
        SELECT * FROM pokemon_information
        WHERE mon_id = {}
        """.format(mon_id))

        results = self.cursor.fetchone()
        self.mon_id = mon_id
        self.evolution_chain_id = results[1]
        self.name = results[2]
        self.first_type = results[3]
        self.second_type = results[4]
        self.height = results[5]
        self.weight = results[6]
        self.hp = results[7]
        self.attack = results[8]
        self.defense = results[9]
        self.special_attack = results[10]
        self.special_defense = results[11]
        self.speed = results[12]
        self.evolutions_list = results[13]
        print(results)

    def load_all_pokemon(self):
        self.cursor.execute("""
        SELECT * FROM pokemon_information
        """)

        results = self.cursor.fetchall()
        print(results)

    def delete_all_pokemon_info(self):
        self.cursor.execute("""
        DELETE FROM pokemon_information
        """)
        self.connection.commit()

def get_evolution_chain(chain_id):
    pokemon_chain_url = api_url_evolution + chain_id
    response = requests.get(pokemon_chain_url)

    try:
        data = response.json()
        data_evolutions_counter = str(data).count("evolves_to")
        evolution_dictionary = {}
        evolution_list = []

        if (evolution_chain_id in special_chain_3):

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][1]["species"]["name"]

        elif (evolution_chain_id in special_chain_4):

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["fourth_pokemon"] = data["chain"]["evolves_to"][0]["evolves_to"][1]["species"]["name"]

        elif (evolution_chain_id in unique_structure_chain_4):

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][1]["species"]["name"]
            evolution_dictionary["fourth_pokemon"] = data["chain"]["evolves_to"][2]["species"]["name"]

        elif (evolution_chain_id in unique_structure_chain_5):

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][1]["species"]["name"]
            evolution_dictionary["fourth_pokemon"] = data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["fifth_pokemon"] = data["chain"]["evolves_to"][1]["evolves_to"][0]["species"]["name"]

        elif (evolution_chain_id in unique_structure_chain_9):

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][1]["species"]["name"]
            evolution_dictionary["fourth_pokemon"] = data["chain"]["evolves_to"][2]["species"]["name"]
            evolution_dictionary["fifth_pokemon"] = data["chain"]["evolves_to"][3]["species"]["name"]
            evolution_dictionary["sixth_pokemon"] = data["chain"]["evolves_to"][4]["species"]["name"]
            evolution_dictionary["seventh_pokemon"] = data["chain"]["evolves_to"][5]["species"]["name"]
            evolution_dictionary["eighth_pokemon"] = data["chain"]["evolves_to"][6]["species"]["name"]
            evolution_dictionary["ninth_pokemon"] = data["chain"]["evolves_to"][7]["species"]["name"]

        elif (data_evolutions_counter == 1):

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]

        elif (data_evolutions_counter == 2):

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]

        elif (data_evolutions_counter == 3):

            evolution_dictionary["initial_pokemon"] = data["chain"]["species"]["name"]
            evolution_dictionary["second_pokemon"] = data["chain"]["evolves_to"][0]["species"]["name"]
            evolution_dictionary["third_pokemon"] = data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]

        for x in evolution_dictionary.values():
            evolution_list.append(x)

        chain_id = data["id"]

        print(evolution_dictionary)
        return evolution_list, chain_id

    except:
        print("Invalid Evolution Chain Number: Enter a Number Between 1-477")
        print("Please note that NOT all pokemon evolution chains are available")

def get_pokemon_information(pokemon_evolution_list,chain_id):
    for pokemon in pokemon_evolution_list:
        pokemon_url = api_url_pokemon + pokemon
        response = requests.get(pokemon_url)
        data = response.json()

        mon_id = data["id"]
        evolution_chain_id = chain_id
        name = data["name"]
        first_type = data["types"][0]["type"]["name"]

        try:
            second_type = data["types"][1]["type"]["name"]
        except IndexError:
            second_type = "null"

        height = data["height"]
        weight = data["weight"]
        hp = data["stats"][0]["base_stat"]
        attack = data["stats"][1]["base_stat"]
        defense = data["stats"][2]["base_stat"]
        special_attack = data["stats"][3]["base_stat"]
        special_defense = data["stats"][4]["base_stat"]
        speed = data["stats"][5]["base_stat"]
        evolutions_list = pokemon_evolution_list

        iterative_pokemon = Pokemon(mon_id, evolution_chain_id, name, first_type, second_type, height, weight,
                                    hp, attack, defense, special_attack, special_defense, speed, evolutions_list)

        iterative_pokemon.insert_pokemon_info(mon_id)

def main_process():
    pass

#Feth Information from the API
x,y = get_evolution_chain(evolution_chain_id)
get_pokemon_information(x,y)




