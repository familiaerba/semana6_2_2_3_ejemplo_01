"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos "baseAlexErba")

db = client.baseAlexErba
coleccion = db.ciudad

# proceso que agrega una lista de documentos
lista = [
{"nombre": "Quito", "poblacion" : "2011388", "superficie":"372,4"},
{"nombre": "Brasilia", "poblacion" : "3015268", "superficie":"5832"},
{"nombre": "Paris", "poblacion" : "2240621", "superficie":"105,4"}
]

coleccion.insert_many(lista)
