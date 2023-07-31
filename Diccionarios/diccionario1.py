#este diccionario nos da a ingresar un animal 
#el diccionario busca y nos muestra su nombre ya sea en español o ingles 


diccionario_animales={       #aqui estamos definiendo que animales vamos a agregar
    "perro":"dog", "gato":"cat", "conejo":"rabbit","serpiente":"snake", "abeja":"bee", "pajaro":"bird", 
    "caballo":"horse", "elefante":"elephant"    
}
def traduccion(animal):
    if animal in diccionario_animales:         #en este bloque de codigo lo que estamos haciendo es que busque 
        return diccionario_animales[animal]    #la traduccion del animal, el if es para saber si si esta en el diccionario 
    else:                                      #y el else es para decirle al usuario que no esta el animal ingresado en el diccionrio 
        return "Animal no encontrado en el diccionario"
    
animal=input("Ingresa un animal en español:")

if animal in diccionario_animales:
    traduccion=traduccion(animal)
    print (f"{animal} en ingles es:{traduccion}")
else:
    print ("Animal no econtrado")






