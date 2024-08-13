from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def lista_partidos(request):
    partidos = [
        {"nombre": "Partido A", "ideologia": "Centro"},
        {"nombre": "Partido B", "ideologia": "Izquierda"},
        {"nombre": "Partido C", "ideologia": "Derecha"},
    ]
    return JsonResponse(partidos, safe=False)