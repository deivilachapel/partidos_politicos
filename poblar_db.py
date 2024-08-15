import os
import django

# Configura Django para usar los modelos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'partidos_politicos.settings')
django.setup()

from partidos.models import Partido

# Datos a insertar
partidos_data = [
    {"nombre": "Partido Revolucionario Moderno PRM", "ideologia": "Socialdemócrata y Liberal, de Centro-izquierda"},
    {"nombre": "Partido de la Liberación Dominicana PLD", "ideologia": "Socialdemócrata y Progresista, de Centro-izquierda"},
    {"nombre": "Partido Reformista Social Cristiano PRSC", "ideologia": "Conservador y Demócrata Cristiano, de Centro-derecha"}
]

# Insertar datos
for data in partidos_data:
    partido = Partido(nombre=data['nombre'], ideologia=data['ideologia'])
    partido.save()

print("Datos insertados correctamente")
