from rest_framework import viewsets
from pokemon_rest_app.serializers import AllPokemonSerializer
from pokemon_rest_app.models import Pokemons, Evolutions
from django_filters.rest_framework import DjangoFilterBackend


class AllPokemonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows All Pokemons to be viewed.
    """
    queryset = Pokemons.objects.all()
    serializer_class = AllPokemonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'mon_id']
    http_method_names = ['get']
























