#en este ejercico vemos los divisores de un numnero ingresado por el usuario
#
#
num=num=int(input("ingrese un numero para saber sus divisores:"))
print (f"los divisores de {num} son:")
for i in range(1,num+1):
    if num%i==0:
        print(i)