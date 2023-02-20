import random
from time import sleep
print('Vamos Jogar Par ou Impar,Até vc perde')
eP=nP=eC=s=v=0
eps=''
while True:
    eC=random.randint(0,10)
    while True:
        eP=int(input('''Vc escolhe
        [1]Par ou
        [2]Impar
        Digite sua escolha:'''))
        if(eP==1 or eP==2):
            break
        else:
            print('Digite um dado valido')
    if(eP==1):
        eps='Par'
    else:
        eps='Impar'
    print(f'Você escolheu {eps}')
    while True:
        nP=int(input('Digite um numero de 0 a 10 quq vc queira jogar:'))
        if(nP>0 and 10>=nP):
            break
        else:
            print('Digite um valor valido')
    sleep(1)
    print('Processando...')
    sleep(1)
    s=eC+eP
    print(f'A soma deu {s}')
    if(eP==1):
        if(s%2==0):
            print(f'Vc venceu dessa vez.{s} é um numero Par')
        else:
            print(f'{s} é um numro impar')
            break
    else:
        if(s%2!=0):
            print(f'Vc venceu dessa vez.{s} é um numro impar')
        else:
            print(f'{s} é um numro par')
            break
    v+=1
if(v==1):
    print(f'Vc perdeu mas ganhou {v} vez')
else:
    print(f'Vc perdeu mas ganhou {v} vezes seguidas')


