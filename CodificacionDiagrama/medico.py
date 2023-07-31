from usuario import *
from consulta import *

class medico (usuario):
    def __init__(self, Nombre,Documento, Telefono,contraseña,consultorio):
        
        self.__nombre=Nombre
        self.__Documento=Documento
        self.__Telefono=Telefono
        self.__contraseña=None
        self.__consultorio=consultorio
        
        
        
        
        
        
        
        
        
        
        
#Setters
    def setNombre (self, nombre):
        self.__nombre=nombre
    
    def setDocumento (self, documento):
        self.__documento=documento
        
    def setTelefono (self, Telefono):
        self.__telefono=Telefono
    
    def setContraseña (self, contraseña):
        self.__contraseña=contraseña
        
    def setConsultorio (self, Consultorio):
        self.__Consultorio=Consultorio
#Getters
    
    def getNombre (self):
        return self.__nombre
    
    def getDocumento (self):
        return self.__documento
    
    def getTelefono (self):
        return self.__telefono
    
    def getContraseña (self):
        return self.__contraseña
    
    def getConsultorio (self,consultorio):
        self.__consultorio=consultorio