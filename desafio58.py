import random
from time import sleep
nA = random.randint(0,10)
nE = 0
c =0
while nE != nA:
    nE = int(input('Adivinhe um numero de 0 a 10:'))
    print('Processando...')
    sleep(1)
    if(nE != nA):
        print('Você errou, tente novamente')
    
        if(nE<nA):
            print('É um numero Maior')
        elif(nE>nA):
            print('É um numero Menor')
    c+=1
print('Você acertou em {} tentativas'.format(c))

