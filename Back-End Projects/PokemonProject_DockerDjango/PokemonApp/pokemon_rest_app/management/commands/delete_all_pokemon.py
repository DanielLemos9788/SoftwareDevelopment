# Django Management Library
from django.core.management.base import BaseCommand
# Internal PokemonApp Model
from pokemon_rest_app.models import Pokemons


class Command(BaseCommand):
    help = ("""Deletes All the Information on the Pokemon Data Base on Postgres
        In Order to Execute the Command Please Follow the Example -->
        python manage.py delete_all_pokemon.py
        """)

    def handle(self, *args, **options):
        Pokemons.objects.all().delete()
        print(f'The Pokemon Data Base was Deleted')



