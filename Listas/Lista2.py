#este programa es con la serie Fibonacci, con la cantidad de 
#dígitos que el usuario desee

def fibonachi(d):
    a=0
    b=1
    for i in range(d):
        a=b+c
        b=c 
        c=a
    return b

numero=int(input("Ingrese la cantidad de digitos que desea:"))
a=[]

for z in range(numero):
    a.append(fibonachi(z))
    print(a)




