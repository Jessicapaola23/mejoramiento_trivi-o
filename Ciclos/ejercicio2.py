#este ejercicio nos muestra si un numero ingresado por el usuario es o no es primo

n=int(input("ingrese un numero para saber si es primo o no:"))
x=1
y=0
while x <= n:
    if n%x==0:
        y=y
        x=x+1
if y ==2:
    print(f'el numero {n} es primo')
else:
    print(f'el numero {n} no es primo')