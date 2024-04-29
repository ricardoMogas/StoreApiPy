from pymongo import MongoClient

# Conexion de la base de datos
client = MongoClient('localhost', 27017)

# Selecciona la base de datos
db = client['StoreDB_Distri']

# Selecciona la colección
collection = db['users']

# Obtener todos los documentos
for documento in collection.find():
    print(documento)
