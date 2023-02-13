from pokemon_rest_app.models import Pokemons, Evolutions
from rest_framework import serializers


class AllPokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemons
        fields = ['mon_id',
                  'name',
                  'evolution_chain_id',
                  'evolutions_list',
                  'first_type',
                  'second_type',
                  'height',
                  'weight',
                  'hp',
                  'attack',
                  'defense',
                  'special_attack',
                  'special_defense',
                  'speed'
                  ]





