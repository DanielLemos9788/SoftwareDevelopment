# Django Management Library
from django.core.management.base import BaseCommand

# Internal PokemonApp Controllers
from pokemon_rest_app.controllers import *


class Command(BaseCommand):
    help = ("""Fetches a Evolution Chain from the Pokemon API
    In Order to Execute the Command Please Follow the Example -->
    python manage.py fetch_pokemon --chain_id 123
    """)

    def add_arguments(self, parser):
        parser.add_argument('--chain_id',
                            dest='chain_id',
                            type=str,
                            required=True,
                            help='Enter a valid chain_id for updated evolutions 1-477')

    def handle(self, *args, **options):
        chain_id = str(options.get('chain_id'))

        try:
            x, y, z = get_evolution_chain(chain_id)
            get_and_save_pokemon_information(x, y, z)

        except ValueError:
            print("Invalid Evolution Chain Number: Enter a Number Between 1-477")
            print("Please note that NOT all pokemon evolution chains are available")

