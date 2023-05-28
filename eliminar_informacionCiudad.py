"""
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.baseAlexErba
coleccion = db.ciudad

print("Proceso para borrar la informacion de una colección")
coleccion.delete_many({})

print("Muestra todos los documentos")
resultado = coleccion.find()
for registro in resultado:
    print(registro)
