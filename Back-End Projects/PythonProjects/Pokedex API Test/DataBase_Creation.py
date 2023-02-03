import sqlite3

#Creation of Data Base on Directory
connection = sqlite3.connect("pokemon_data_base.db")
cursor = connection.cursor()

#Creation of Pokemon Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS pokemon_information (
    mon_id INTEGER,
    evolution_chain_id INTEGER,
    name TEXT,
    first_type TEXT,
    second_type TEXT,
    height INTEGER,
    weight INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    special_attack INTEGER,
    special_defense INTEGER,
    speed INTEGER,
    evolutions_list TEXT
)
""")

connection.commit()
connection.close()

