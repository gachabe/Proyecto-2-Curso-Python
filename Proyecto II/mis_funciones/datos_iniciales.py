import json
import requests
from mis_funciones import BBDD as bd
from mis_funciones import listas as l
"""
Aqui haremos una carga inicial de los datos
"""

def busca_artista(nombre):
    """

    función para poder buscar de forma rápida los JSON que subiremos a nuestra base de datos
    """

    response = requests.get(f'https://itunes.apple.com/search?term={nombre}')
    json_data = json.loads(response.text)
    resultado = json_data["results"]
    if resultado != []:
        for i in resultado:
            if (i['artistName']) == nombre:
                print(f" Nombre =  {i['trackName']}, Id = {i['trackId']}, Albúm = {i['collectionCensoredName']} ")
    else:
        raise Exception("Error en la búsqueda")

def volcado_artista(nombre):
    """

    función para poder crear una base de canciones inicial
    """

    response = requests.get(f'https://itunes.apple.com/search?term={nombre}')
    json_data = json.loads(response.text)
    resultado = json_data["results"]
    if resultado != []:
        i = 0
        j = 0
        while j < 5:
            if (resultado[i]['artistName']) == nombre:
               bd.crear_cancion(resultado[i]['trackId'],resultado[i]['trackName'],resultado[i]['artistName'],
                                resultado[i]['primaryGenreName'],
                                resultado[i]['collectionCensoredName'],resultado[i]['trackViewUrl'])
               j += 1
               i +=1
            else:
               i += 1
        print(f"El artista {nombre} fue añadido de forma satisfactoria")
    else:
        raise Exception("Error en la búsqueda")


volcado_artista("Estopa")
volcado_artista("Triana Pura")
volcado_artista("Mecano")
volcado_artista("SFDK")
volcado_artista("Mägo de Oz")
volcado_artista("Gloria Gaynor")
volcado_artista("ABBA")
volcado_artista("Santana")
volcado_artista("Bee Gees")
volcado_artista("Tom Jones")


 #listas preestablecidas
canciones1 = [ i
    for i in bd.db.canciones.find({"cantante": "Estopa"})
]

lista1 = l.PlayList("estopa","Admin",canciones1)

canciones2 = [ i
    for i in bd.db.canciones.find({"cantante": "SFDK"})
]
lista2 = l.PlayList("sfdk","Admin",canciones2)

canciones3 = [ i
    for i in bd.db.canciones.find({"cantante": "ABBA"})
]
lista3 = l.PlayList("mamma mia","Admin",canciones3)
lista4 = l.PlayList("vacia","Admin",[]) #Esta lista es para demostrar que se pueden crear listas vacias, que es algo
#que he considerado que se debería de poder