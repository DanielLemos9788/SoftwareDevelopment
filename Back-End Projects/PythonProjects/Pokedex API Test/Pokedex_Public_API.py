"""from flask import Flask

app = Flask(__name__)

@app.get('/')
def home_page():
    data_set = {"Result": "Server Online"}
    return data_set

@app.get('/pokemon/')
def request_page():
    pokemon_query = "Charizard"
    return pokemon_query

"""
from fastapi import FastAPI
#import requests
#import sqlite3


app = FastAPI()

@app.get('/')
def initial_page():
    return{"Response": "Pokedex Server Online"}

@app.get('/pokemon/{mon_id}')
def load_pokemon_response(mon_id: int):
    mon_id = mon_id
    print(mon_id)

