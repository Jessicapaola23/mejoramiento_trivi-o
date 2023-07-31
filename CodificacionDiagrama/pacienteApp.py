from usuario import *
from Paciente import *
from medico import *


usuarios_registrados = {
        "sara": "12345",
        "Raul": "98752",
        "andres": "12345",
        "julian": "12345",
     
    }
#usuarios= usuarios_registrados(usuarios_registrados)

horaCita={
        1:"1.cita medicina general 30 de julio, Hora: 14:00",
        2:"2.cita medicina general 28 de julio, Hora: 09:00",
        3:"3.cita medicina general 29 de julio, Hora: 10:00",
        4:"4.cita medicina general 09 de agosto, Hora: 15:00",
        5:"5.cita medicina general 10 de agosto, Hora: 13:00",
    }
#hora=paciente(horaCita)

def menu():
    print("MENÚ\n")
    print("1. iniciar sesion")
    print("2.mostrar fechas disponibles ")
    print("3.Escoger especialidad")
    print("4.Consultorios Disponibles")
    print("5.ver informacion sobre la cita")
    print("6.Eliminar cita")
    print("7.Finalizar")