#llenar dos listas con numeros aleatorios y decir cual de las dos listas tiene
#el numero menor
import random
lista1=[]
lista2=[]
tam=int(random.randint(1,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista1.append(num)

lista2.append(num)

print(lista1)
print(lista2)


