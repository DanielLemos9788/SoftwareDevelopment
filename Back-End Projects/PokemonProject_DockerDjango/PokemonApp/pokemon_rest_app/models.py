from django.db import models


class Pokemons(models.Model):
    mon_id = models.CharField(max_length=250)
    evolution_chain_id = models.CharField(max_length=250)
    name = models.CharField(primary_key=True, max_length=250)
    first_type = models.CharField(max_length=250)
    second_type = models.CharField(blank=True, max_length=250)
    height = models.CharField(blank=True, max_length=250)
    weight = models.CharField(blank=True, max_length=250)
    hp = models.CharField(blank=True, max_length=250)
    attack = models.CharField(blank=True, max_length=250)
    defense = models.CharField(blank=True, max_length=250)
    special_attack = models.CharField(blank=True, max_length=250)
    special_defense = models.CharField(blank=True, max_length=250)
    speed = models.CharField(blank=True, max_length=250)
    evolutions_list = models.CharField(blank=True, max_length=250)


class Evolutions(models.Model):
    evolution_chain_id = models.CharField(max_length=250)
    name = models.CharField(primary_key=True, max_length=250)
    evolution_type = models.CharField(blank=True, max_length=250)
    pokemon = models.ForeignKey(Pokemons, on_delete=models.CASCADE)




