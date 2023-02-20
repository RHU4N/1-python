import random
from time import sleep
nA = random.randint(0,5)

nE = int(input('Adivinhe um numero de 0 a 5:'))

print('Processando...')
sleep(3)
if(nE == nA):
    print('Você acertou o número!!!')
else:
    print('Você errou!!!')