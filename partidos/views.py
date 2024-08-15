from django.http import JsonResponse
from .models import Partido

def lista_partidos(request):
    partidos = Partido.objects.all()
    partidos_list = list(partidos.values('nombre', 'ideologia'))
    return JsonResponse(partidos_list, safe=False)
