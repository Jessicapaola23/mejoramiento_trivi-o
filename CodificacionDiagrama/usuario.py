class usuario:
    def __init__ (self,id,nombre,documento,telefono,contraseña):
       self.__id=id
       self.__nombre=nombre
       self.__documento=documento
       self.__telefono=telefono
       self.__contraseña=contraseña

#Setters
    def setNombre (self, nombre):
        self.__nombre=nombre
    
    def setDocumento (self, documento):
        self.__documento=documento
        
    def setTelefono (self, Telefono):
        self.__telefono=Telefono
    
    def setContraseña (self, contraseña):
        self.__contraseña=contraseña
#Getters
    def getId (self):
        return self.__id
    
    def getNombre (self):
        return self.__nombre
    
    def getDocumento (self):
        return self.__documento
    
    def getTelefono (self):
        return self.__telefono
    
    def getContraseña (self):
        return self.__contraseña