from usuario import *
from consulta import *

class paciente (usuario):
    def __init__(self,Nombre,documento, Telefono,contraseña,consultorio ):
        self.__nombre=Nombre
        self.__documento=documento
        self.__Telefono=Telefono
        self.__contraseña = None
        self.__consultorio=consultorio

#setters
    
def setNombre (self, Nombre):
        self.__nombre = Nombre

def setDocumento (self,documento):
       self.__documento=documento

def setTelefono (self, Telefono):
        self.__telefono = Telefono
    
def setContraseña (self, contraseña):
        self.__contraseña=contraseña

def setCosultorio(self, consultorio):
        self.__consultorio=consultorio
#Getters 

def getNombre (self):
        return self.__nombre
    
def getDocumento (self):
        return self.__documento

def getTelefono (self):
        return self.__telefono

def getContraseña (self):
        return self.__contraseña

def getConsultorio(self):
        return self.__Consultorio