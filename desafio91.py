from operator import itemgetter
from random import randint
from time import sleep

# jogadores=dict()
# for c in range(1,5):
#     dado=randint(1,6)
#     print(f'O jogador {c} tirou {dado}')
#     jogadores['jogador']=f'jogador {c}'
#     jogadores['dado']=dado
# print(jogadores)

jogo = {'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6),}
ranking=dict()
print('valores sorteados')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print(ranking)
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]}')
    sleep(1)