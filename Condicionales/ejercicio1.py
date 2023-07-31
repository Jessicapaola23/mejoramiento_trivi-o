#Escribe un programa que pida tres números y que escriba si son los tres iguales
#si hay dos iguales o si son los tres distintos
v1=int(input("Ingrese el valor 1:"))
v2=int(input("Ingrese el valor 2:"))
v3=int(input("Ingrese el valor 3:"))
print(v1,v2,v3)

def valores_iguales():
    if v1 == v2 == v3:
        print("Los tres valores son iguales")
    elif v1 != v2 == v3:
        print("El valor 2 y 3 son iguales")
    elif v1 == v2 != v3:
        print("El valor 1 y 2 son iguales")
    elif v2 != v3 == v1:
        print("El valor 1 y 3 son iguales")
    elif v1 != v2 != v3:
        print("Los tres valores son diferentes")




valores_iguales()