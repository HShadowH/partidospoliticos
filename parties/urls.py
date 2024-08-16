from django.urls import path
from .views import political_parties_list

urlpatterns = [
    path('api/political-parties/', political_parties_list, name='political_parties_list'),
]
