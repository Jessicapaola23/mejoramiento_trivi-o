#este codigo es para saber un numero natural

def numnat(x):
    suma=1
    n=1
    while suma <= maximo:
        suma=suma+n
        n=n+1
    return n-1
maximo=int(input("introduce un numero maximo:"))
lista=numnat(-1)
print(f"el numero natural mas pequeño necesario para superar el maximo es:{lista}")


