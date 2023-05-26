#Conexión con el servidor
from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://Admin:mongopass@cluster0.hjgtzo4.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Conexión correcta con el servidor")
except Exception as e:
    print(e)

db = client.ListaReproduccion


#Creación de las colecciones
"""
Aqui crearemos las colecciones dentro de la base de datos, mostrando el debido error en caso de ya existir
"""


try:
    db.create_collection("canciones")
    print("Colección canciones creada correctamente")
except Exception as e:
    print(e)

try:
    db.create_collection("listas")
    print("Colección listas creada correctamente")
except Exception as e:
    print(e)

try:
    db.create_collection("usuarios")
    print("Colección usuarios creada correctamente")
except Exception as e:
    print(e)


#Funciones de gestión
"""
Aqui crearemos las funciones necesarias para la creación y manejo de las distintas colecciones
"""


# Funcion de creacion de autores

def crear_usuario(usuario, nombre, apellido, correo):
    "Creará un nuevo usuario en la bse de datos si es posible"
    cursor = db.usuarios.find_one({"_id": usuario})
    if cursor is None:
        usuario = ([{
            "_id": usuario,
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo


        }])
        db.usuarios.insert_many(usuario)

    else:
        Exception("El usuario ya existe...")

def crear_cancion(id,nombre,cantante,genero,album,url):
    "añadirá una nueva canción a la base de datos si es posible"
    cursor = db.canciones.find_one({"_id": id})
    if cursor is None:
        cancion= ([{"_id": id,
                       "nombre": nombre,
                       "cantante": cantante,
                       "genero":genero,
                       "album":album,
                       "url":url
                       }])
        db.canciones.insert_many(cancion)
    else:
        Exception("Canción ya existente")

def crear_lista(nombre,usuario,canciones):
    "Creará una lista de reproducción nueva en la base de datos, si es posible"
    cursor = db.listas.find_one({"_id": nombre})
    if cursor is None:
        cancion= ([{"_id": nombre,
                       "usuario": usuario,
                       "canciones" :canciones
                       }])
        db.listas.insert_many(cancion)
    else:
        Exception("Base de datos ya existente")

#Usuarios preestablecidos
crear_usuario("Admin","Admin","admin","Admin@Admin.com")
crear_usuario("Gabriel","Gabriel","Chaves","gachaben@us.es")
crear_usuario("almhorpar","Almudena","Horcas","almhorpar@us.es")

