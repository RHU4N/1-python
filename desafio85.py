par=list()
impar=list()
numeros=list()
for c in range(0,7):
    n=float(input('Digite um número:'))
    if(n%2==0):
        par.append(n)
    elif(n%2!=0):
        impar.append(n)

    par.sort()
    impar.sort()
numeros.append(par[:])
numeros.append(impar[:])
print(f'Esses são os numeros pares {numeros[0]} e esses são os impares {numeros[1]} ')
