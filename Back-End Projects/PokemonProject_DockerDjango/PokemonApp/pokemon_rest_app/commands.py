# Internal Controllers
from pokemon_rest_app.controllers import *

# Django
from django.core.management.base import BaseCommand

chain_id = '1'
x, y = get_evolution_chain(chain_id)
get_and_save_pokemon_information(x, y)




