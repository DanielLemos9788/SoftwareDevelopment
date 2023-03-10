from django.urls import include, path
from rest_framework import routers
from pokemon_rest_app import views

router = routers.DefaultRouter()
router.register(r'all_pokemons', views.AllPokemonViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


