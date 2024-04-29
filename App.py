from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Conexión a la base de datos
client = MongoClient('localhost', 27017)
db = client['StoreDB_Distri']
collection = db['users']

@app.route('/users', methods=['GET'])
def obtener_usuarios():
    usuarios = list(collection.find({}, {'_id': False}))
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)
