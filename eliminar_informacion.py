"""
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.baseAlexErba
coleccion = db.pais

print("Proceso para borrar la informacion de una colección")
coleccion.delete_many({})

print("Muestra todos los documentos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)
