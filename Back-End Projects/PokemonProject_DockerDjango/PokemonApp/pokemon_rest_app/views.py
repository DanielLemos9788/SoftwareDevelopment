from rest_framework import viewsets
from pokemon_rest_app.serializers import AllPokemonSerializer, SinglePokemonSerializer
from pokemon_rest_app.models import Pokemons, Evolutions
from django_filters.rest_framework import DjangoFilterBackend


class AllPokemonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows All Pokemons to be viewed.
    """
    queryset = Pokemons.objects.all()
    serializer_class = AllPokemonSerializer
    http_method_names = ['get']


class SinglePokemonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows One Pokemon to be viewed.
    """
    queryset = Pokemons.objects.all()
    serializer_class = SinglePokemonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'mon_id']
    http_method_names = ['get']






















