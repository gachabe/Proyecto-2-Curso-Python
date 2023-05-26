from mis_funciones import BBDD as bd
from mis_funciones import listas as l
from mis_funciones import datos_iniciales #Para hacer la carga inicial cuando se llame en el Main
db = bd.client.ListaReproduccion

def crearlista(nombre,user = "Admin"):
    try:
        cursor = db.listas.find({"_id": nombre})
        for c in cursor:
            canciones = c["canciones"]
        return(l.PlayList(nombre,user,canciones))
    except:
        Exception("Nombre erroneo de la base")




def menu():
    estado = True
    print("---      PROYECTO II       ---")
    print("--- Gabriel Chaves Benítez ---")
    user = input("Diga su usuario, si no esta en la base de datos se le registrará: \n")
    if not l.comprueba_usuario(user):
        nombre = input("Usuario no encontrado, introduzca su nombre para el registro:\n ")
        apellido = input("Introduzca su apellido: ")
        correo = input("Introduzca su correo: ")
        bd.crear_usuario(user, nombre, apellido, correo)

    print(f"Hola {user} ")
    while estado:
        def eleccion():

            print("Introduzca la acción a realizar")
            print("introduce 0 para ver tus listas de reproducción")
            print("Introduce 1 para crear una lista de reproducción")
            print("Introduce cualquier otra cosa para salir")
            elecc = int(input(""))
            if elecc not in [0, 1, 2]:
                print("Elección no válida")
                eleccion()
            else:
                return elecc
        elecc = eleccion()
        if elecc == 0:
            print("Te muestro todas tus listas de reproducción: ")
            l.PlayList.consultar_playlist(user)
            elecc = input("elija la lista de reproducción que quieras ver \n")
            lista = crearlista(elecc, user)
            Nelecc =  int(input("¿Quieres que te muestre tu playlist sin el género (0) o con el genero(1)? "))
            if Nelecc not in [0, 1]:
                print("Eleccion equivocada, paso a mostrar la lista sin genero ")
                print(lista.mostrar_canciones())
            elif Nelecc == 0:
                print("Mostrando la lista con el género por canción: ")
                print(lista.mostrar_canciones())
            elif Nelecc == 1:
                print("Mostrando la lista sin el género por canción: ")
                lista.mostrar_playlist()
            estado = False
        elif elecc == 1:
            nombre = input("Introduce el nombre de la lista")
            nueva = crearlista(nombre,user)
            print("Ahora mismo tu lista esta vacía, aquí te dejo unas recomendaciones")
            nueva.anadir_cancion()
        else:
            print("Cerrando la aplicación, Gracias ")
            estado = False








