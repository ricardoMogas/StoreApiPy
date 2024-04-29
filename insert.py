from pymongo import MongoClient

# Conexión a la base de datos
client = MongoClient('localhost', 27017)

# Selecciona la base de datos
db = client['StoreDB_Distri']

# Selecciona la colección
collection = db['users']

# Inserta un documento
documento = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
insert_result = collection.insert_one(documento)

print("Documento insertado con el ID:", insert_result.inserted_id)
