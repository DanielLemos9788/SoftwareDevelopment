from flask import Flask
import sqlite3

app = Flask(__name__)
@app.get('/')
def initial_page():
    data_set = {"Response": "Pokedex Server Online"}
    return data_set

@app.get('/all_pokemon_list/')
def list_all_pokemon_page():
    connection = sqlite3.connect("pokemon_data_base.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokemon_information")
    result = cursor.fetchall()
    return result

@app.get('/pokemon/<name>')
def single_pokemon_page(name):
    pokemon_dictionary = {"mon_id":"",
                          "name":"",
                          "first_type":"",
                          "second_type":"",
                          "height":"",
                          "weight":"",
                          "hp":"",
                          "attack":"",
                          "defense":"",
                          "special_attack":"",
                          "special_defense":"",
                          "speed":"",
                          "evolution_chain_id":"",
                          "evolution_list":""}

    connection = sqlite3.connect("pokemon_data_base.db")
    cursor = connection.cursor()
    cursor.execute("""
            SELECT * FROM pokemon_information
            WHERE name = {}
            """.format(name))

    results = cursor.fetchone()

    pokemon_dictionary["mon_id"] = results[0]
    pokemon_dictionary["evolution_chain_id"] = results[1]
    pokemon_dictionary["name"] = results[2]
    pokemon_dictionary["first_type"] = results[3]
    pokemon_dictionary["second_type"] = results[4]
    pokemon_dictionary["height"] = results[5]
    pokemon_dictionary["weight"] = results[6]
    pokemon_dictionary["hp"] = results[7]
    pokemon_dictionary["attack"] = results[8]
    pokemon_dictionary["defense"] = results[9]
    pokemon_dictionary["special_attack"] = results[10]
    pokemon_dictionary["special_defense"] = results[11]
    pokemon_dictionary["speed"] = results[12]
    pokemon_dictionary["evolutions_list"] = results[13]

    return pokemon_dictionary


app.run(port=7777, debug=True)

