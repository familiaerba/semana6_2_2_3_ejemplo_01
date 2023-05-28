"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos "baseAlexErba")

db = client.baseAlexErba
coleccion = db.pais

# proceso que agrega una lista de documentos
lista = [
{"nombre": "Ecuador", "idioma": "Español", "presidente":"Guillermo Lasso", "siglas":"ECU"},
{"nombre": "Brazil", "idioma": "Portugués", "presidente":"Luiz Inácio Lula da Silva", "siglas":"BRA"},
{"nombre": "Francia", "idioma": "Frances", "presidente":"Emmanuel Macron", "siglas":"FRA"}
]

coleccion.insert_many(lista)
