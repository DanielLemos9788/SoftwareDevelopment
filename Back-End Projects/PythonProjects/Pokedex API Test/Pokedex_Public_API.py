from flask import *
import json, time

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home_page():
    data_set = {"Page": "Home", "Message": "Successfully Loaded Home Page", "Timestamp": time-time()}
    json_dump = json.dump(data_set)
    return json_dump

@app.route("/pokemon/", methods=["GET"])
def request_page():
    pokemon_query = str(request.args.get("pokemon")) #/pokemon/?=XXX

    data_set = {"Page": "Home", "Message": f"Successfully Request for {pokemon_query}", "Timestamp": time-time()}
    json_dump = json.dump(data_set)
    return json_dump

app.run(port=7777)
request_page()
