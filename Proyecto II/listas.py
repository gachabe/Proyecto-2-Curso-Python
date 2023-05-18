import  BBDD as bd
from random import randint
db = bd.client.ListaReproduccion

def comprueba_usuario(usuario):
    """
    Comprobamos si el nombre dado es un usuario

    """
    estado = False
    cursor = db.usuarios.find()
    for c in cursor:
        if c["_id"] == usuario:
            estado = True
    return estado

class PlayList:
    """
    nombre: nombre de la lista
    usuario: usuario que creó la lista
    canciones: diccionario que esta compuesto por subdiccionarios que son las canciones. La estructura es la siguiente:
    { id_cancion1 : {nombre: nombre_cancion , cantante : nombre_cantante album:album_cancion, género: genero_cancion
     url : url_cancion},
      id_cancion2: {nombre: nombre_cancion , cantante : nombre_cantante album:album_cancion,
      genero: genero_cancion, url : url_cancion}}
    """
    def __init__(self,nombre,usuario,canciones=[]):
        self.nombre = nombre
        if comprueba_usuario(usuario):
            self.usuario = usuario
        self.canciones = canciones
        bd.crear_lista(self.nombre, self.usuario, self.canciones)

    def __str__(self):
        cancionstr = ""
        cursor = db.listas.find({"_id":self.nombre})
        for c in cursor:
            for tema in c["canciones"]:
                cancion = tema["nombre"]
                cantante = tema["cantante"]
                genero = tema["genero"]


                cancionstr += f"Tema: {cancion}\nGrupo: {cantante}  \n"

        return cancionstr
    def  mostrar_canciones(self):
        return (str(self))

    def mostrar_sugerencias(self, add = False):
        """
        Aquí  no tenía claro si se supone que sé cuantos elementos tiene mi base de datos canciones, asi que usaré
        una solución que, a priori, no sabe cuantas canciones hay
        :return:
        """
        print("\n-- Estas son mis 20 recomendaciones para ti --")
        cursor = db.canciones.find()
        n = 0
        recomendacion = []
        while n < 20:
            x = randint(0,1)
            c = (next(cursor)["nombre"])
            if x == 1:
                print(n," - ",c)
                n += x
                if add:
                    recomendacion.append(c)
        if add:
            return recomendacion
    def anadir_cancion(self):
        lista = self.mostrar_sugerencias(True)
        eleccion = int(input("Elige una canción para añadir a la lista. Elige 20 para salir \n"))

        def comprobacion(eleccion):
            if eleccion > 20:
                print("Número equivocado")

            elif eleccion == 20:
                return
            elif eleccion < 20:

                cancion = lista[eleccion]
                cursor = db.canciones.find({"nombre": cancion})
                adicion = next(cursor)
                db.listas.update_one({"_id": self.nombre},
                                       {"$push": {"canciones":adicion}})
        comprobacion(eleccion)

    @staticmethod
    def consultar_playlist(usuario):
        cursor = db.listas.find()
        print("\n Las listas de este usuario son: \n")
        for c in cursor:
            if c["usuario"] == usuario:
                print(c["_id"])
        print("\n Además, tambien están estas playlist preestablecidas: \n")
        cursor = db.listas.find()
        for c in cursor:
            if c["usuario"] == "Admin":
                print(c["_id"])


    #AQUI COMIENZA MI ERROR
    @staticmethod
    def decorador(fun):
        def wrapper(self, *args, **kwargs):
            a = fun(self, *args, **kwargs).split("\n")
            b = []
            cursor = db.listas.find({"_id": self.nombre})

            for c in cursor:
                for tema in c["canciones"]:
                    genero = tema["genero"]
                    b.append(genero)

            cancionstr = []
            for j in range(len(b)):
                cancionstr.append(a[0 + 2 * j])
                cancionstr.append(a[1 + 2 * j])
                cancionstr.append((f"Genero: {b[j]}"))
            for i in cancionstr:
                print(i)


        return wrapper

    @decorador
    def mostrar_playlist(self):
        return self.mostrar_canciones()

        #AQUI TERMINA


 #listas preestablecidas
canciones1 = [ i
    for i in bd.db.canciones.find({"cantante": "Estopa"})
]

lista1 = PlayList("estopa","Admin",canciones1)

canciones2 = [ i
    for i in bd.db.canciones.find({"cantante": "SFDK"})
]
lista2 = PlayList("sfdk","Admin",canciones2)

canciones3 = [ i
    for i in bd.db.canciones.find({"cantante": "ABBA"})
]
lista3 = PlayList("mamma mia","Admin",canciones3)
lista4 = PlayList("vacia","Admin",[])

lista2.mostrar_playlist()
