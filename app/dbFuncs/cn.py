import json
from pymongo import MongoClient

def get_user():
    with open('../credentials.json', 'r') as f: #llamamos al archivo credentials.json
        json_str = f.read()
        credenciales = json.loads(json_str)
        return credenciales['dbUser']

def connect():
    client = MongoClient(get_user())
    Collection = client.Usuarios #?
    Tabla = Collection.Autenticacion
    return Tabla
