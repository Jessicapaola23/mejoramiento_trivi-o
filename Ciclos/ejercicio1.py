num=num=int(input("ingrese un numero para saber sus divisores:"))
print (f"los divisores de {num} son:")
for i in range(1,num+1):
    if num%i==0:
        print(i)
     
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