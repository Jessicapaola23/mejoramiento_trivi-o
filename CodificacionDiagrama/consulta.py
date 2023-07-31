from Paciente import*
from medico import*
class Consulta:
    def __init__(self,fecha_disponible,hora_disponible,motivo_cita,eliminar_cita):
       self.__fecha_disponible=fecha_disponible
       self.__hora_disponible=hora_disponible
       self.__motivo_cita=motivo_cita
       self.__eliminar_cita=eliminar_cita
    
    def agendar_cita_paciente (fecha_disponible,hora_disponible,motivo_cita,eliminar_cita,self, 
                               Nombre,documento, Telefono,contraseña):
        print ("Deseas realizar el agendamiento no superior a un mes:")
        print ("1.Si")
        print ("2.No")
        selector = int(input())
        match selector:
            case 1:
                    self.__agendar = "Agendamiento de citas"
                    obj1 = paciente(Nombre ,documento, Telefono ,contraseña)
                    obj2 = Consulta(fecha_disponible,hora_disponible,motivo_cita,eliminar_cita)
                    self.__nombre.append(Nombre)
                    self.__documento.append(documento)
                    self.__telefono.append(Telefono)    
                    self.__contraseña=contraseña
                    self.__fecha_disponible=fecha_disponible
                    self.__hora_disponible=hora_disponible
                    self.__motivo_cita=motivo_cita
                    self.__eliminar_cita=eliminar_cita
                    return self.__agendar
            case 2:
                    print("No agendaste la cita")
                    
    
    
    
    
    
    
#setters   
def setfecha_disponible (self,fecha_disponible):
       self.__fecha_disponible= fecha_disponible


def setHora__disponible (self,hora_disponible):
       self.hora_disponible=hora_disponible

def setmotivo (self,motivo):
       self.motivo=motivo

def setNombre (self, Nombre):
        self.__nombre = Nombre

def setDocumento (self,documento):
        self.__documento=documento
    
def setTelefono (self, Telefono):
        self.__telefono = Telefono
    
def setContraseña (self,contraseña):
        self.__contraseña=contraseña

#Getters
def getfecha_disponible(self):
       return self.__fecha_disponible

def gethora_disponible(self):
       return self.__hora_disponible

def getmotivo (self):
        return self.__motivo
    
def getNombre (self):
        return self.__nombre

def getDocumento (self):
      return self.documento

def getTelefono (self):
        return self.__telefono
      
def getContraseña(self):
        return self.__contraseña