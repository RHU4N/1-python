pessoas=list()
dados=list()
pessoa=0
while True:
    nome=str(input('Digite seu nome: '))
    dados.append(nome)
    print('Adicionado com sucesso')
    peso=float(input('Digite seu peso: '))
    dados.append(peso)
    print('Adicionado com sucesso')
    pessoas.append(dados[:])
    dados.clear()
    pessoa+=1
    while True:
        c = str(input('Quer continuar?[S/N]')).upper().strip()
        if(c[0]=='S' or c[0]=='N'):
            break
    if(c[0]=='N'):
        break
print(f'Foram cadastradas {pessoa} pessoas \n')
print('Pessoas mais pessadas que 80kg:')
for p in pessoas:
    if p[1] >80:
        print(p)
print('pessoas mais leves que 80kg:')
for p in pessoas:
    if(p[1]<80):
        print(p)
    