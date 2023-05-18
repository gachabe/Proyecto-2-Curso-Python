import BBDD as bd
import datos_iniciales as di
import listas as l
db = bd.client.ListaReproduccion


def menu():
    estado = True
    print("---      PROYECTO II       ---")
    print("--- Gabriel Chaves Benítez ---")
    user = input("Diga su usuario, si no esta en la base de datos se le registrará: ")
    if not l.comprueba_usuario(user):
        nombre = input("Usuario no encontrado, introduzca su nombre para el registro: ")
        apellido = input("Introduzca su apellido: ")
        correo = input("Introduzca su correo: ")
        bd.crear_usuario(user, nombre, apellido, correo)

    print(f"Hola {user} ")
    def eleccion():

        print("Introduzca la acción a realizar")
        print("introduce 0 para ver tus listas de reproducción")
        print("Introduce 1 para crear una lista de reproducción")

        elecc = int(input(""))
        if elecc not in [0, 1, 2]:
            print("Elección no válida")
            eleccion()
        else:
            return elecc
    elecc = eleccion()
    if elecc == 0:
        l.PlayList.consultar_playlist(user)
        elecc = input("elija la lista de reproducción que quieras ver")
        l.
    elif elecc == 1:
        nombre = input("Introduce el nombre de la lista")
        nueva = l.PlayList(nombre,user)
        print("Ahora mismo tu lista esta vacía, aquí te dejo unas recomendaciones")
        nueva.anadir_cancion()








menu()