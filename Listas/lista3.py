import random
#ejercicio 1                                              #esta dando valores aleatorios con la funcion de python random
def llenarLista(tam,rango):                               #el for lo quie esta haciendo es buscar en la lista
    lista=[random.randrange(rango) for i in range(tam)]   #en este bloque de codigo lo que esta haciendo 
    return lista                                          #es crear la duncion para llenar una lista, cada vez que se llame se va allenar una lista  

def sumaLista(lista):                 #crea la funcion simalista para que sume los numeros de la lista aleatoria
    sum=0                             #el for x un lista esta sumando cada numero de la lista 
    for x in lista:                   #retorna el resultado de la suma
        sum+=x
    return sum

def promedioLista(lista):              #se crea la funcion,
    return sumaLista(lista)/len(lista)

def numMayor(lista):
    mayor=0
    for a in lista:
        if a > mayor:
            mayor=a
    return mayor

def numMenor(lista):
    menor=100000
    for x in lista:
        if menor > x:
            menor=x
    return menor

def ordenAscendente(lista):                                                                                 
    f=len(lista)
    for j in range(f-1):
        for d in range(j+1,f):
            if lista[j]>lista[d]:
                lista[j],lista[d]=lista[d],lista[j]
    return lista

def ordenDescendente(lista):                                                                                 
    f=len(lista)
    for j in range(f-1):
        for d in range(j+1,f):
            if lista[j]<lista[d]:
                lista[j],lista[d]=lista[d],lista[j]
    return lista
def encontrarMediana(lista):
    listaOrdenada=(lista)
    longitud=len(listaOrdenada)
    if longitud %2==0:
        ind1=longitud//2
        ind2=ind1-1
        mediana=(listaOrdenada[ind1])
    else:
        ind1=longitud//2
        mediana=listaOrdenada[ind2]
        return mediana
l1=llenarLista(5,10)
print("la lista aleatoria es",l1)
print("La suma de los valores es la lista es:",sumaLista(l1))
print("El promedio de la lista es:",round(promedioLista(l1), 2))
print("El numero mayor es:",numMayor(l1))
print("El numero menor es:",numMenor(l1))
print("Orden Ascendente:",ordenAscendente(l1))
print("Orden Descendente:",ordenDescendente(l1))
print("La mediana es:",ordenDescendente(l1))