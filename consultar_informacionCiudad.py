"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.baseAlexErba
coleccion = db.ciudad

print("Muestra todos los documentos de la base de datos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)

