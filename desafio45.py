import random
import time

jogadas = ('Pedra','Papel','Tesoura')

com= random.randint(0,2)

print('''Escolha sua opção
[1]Pedra
[2]Papel
[3] Tesoura''')
pl=int(input('Escolha uma das opções:'))-1

print('jo')
time.sleep(1)
print('ken')
time.sleep(1)
print('po')
time.sleep(2)
print('='*11)

if(com==0): #comp jogou pedra
    if(pl==0):
        print('Empate')
    elif(pl==1):
        print('Vc ganhou')
    elif(pl==2):
        print('Vc perdeu')

elif(com==1): #comp jogou papel
    if(pl==1):
        print('Empate')
    elif(pl==2):
        print('Vc ganhou')
    elif(pl==0):
        print('Vc perdeu')

elif(com==2): #comp jogou tesoura
    if(pl==2):
        print('Empate')
    elif(pl==0):
        print('Vc ganhou')
    elif(pl==1):
        print('Vc perdeu')

print('='*11)
print('Computador:',jogadas[com])
print('Player:',jogadas[pl])