from random import randint
from time import sleep
numeros=list()
mega=list()
cont=0
q=int(input('Quantos jogos vc quer: '))
while True:
    for c in range(0,6):
        numeros.append(randint(1,60))
    mega.append(numeros[:])
    numeros.clear()
    cont+=1
    if(cont==q):
        break
for c,j in enumerate(mega):
    print(f'jogo {c+1}:{j}')
    sleep(1)
