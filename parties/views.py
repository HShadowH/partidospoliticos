from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import PoliticalParty
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a la API de Partidos Políticos</h1>")


def political_parties_list(request):
    parties = list(PoliticalParty.objects.values())
    return JsonResponse(parties, safe=False)
