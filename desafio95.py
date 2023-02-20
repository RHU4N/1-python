time=dict()
jogador=dict()
partidas=list()
while True:
    jogador.clear
    jogador['nome']=str(input('Nome jogador: '))
    tot=int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0,tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}?')))
    jogador['gols']=partidas[:]
    jogador['total']= sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Dado invalido')
    if resp == 'N':
        break
print('-='*35)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print('-='*35)
for k,v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*35)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca==999:
        break
    if busca>=len(time):
        print(f'Não existe jogador com esse codigo {busca}')
    else:
        print(f'--Levantamento do jogador {time[busca]["nome"]}')
        for i,g in enumerate(time[busca]["gols"]):
            print('     No jogo {i} fez {g} gols')
    print('-='*35)
print('<<Volte sempre>>')
