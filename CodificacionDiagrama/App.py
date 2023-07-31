from usuario import *
from medico import *
#from Apppaciente import nombre,i,cons


usuarios_registrados = {
        "Jose": "12345",
        "Rodriguez": "12345",
        "Miguel": "12345",
        "Ana": "12345",
     
    }
inicio_sesion = usuario(usuarios_registrados)

mi_agenda = medico()

def mostrar_menu():
    print("----- Menú -----")
    print("1.iniciar sesion")
    print("2. Agendar día")
    print("3. Mostrar días agendados")
    print("4.Consultar nombre del paciente")
    print("5.Consultar motivo de la cita")
    print("6.Consultario de la cita")
    print("8. Salir")
    
continuar=True   

while continuar:
    print("")
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")
    print("")

    if opcion == "1":
        nombre=[]
        usuario_ingresado = input("Ingresa tu nombre de usuario: ")
        contrasena_ingresada = input("Ingresa tu contraseña: ")
        nombre.append(usuario_ingresado)