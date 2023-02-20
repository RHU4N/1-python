pessoa=dict()
galera=dict()
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome: '))
    while True:
        pessoa['sexo']=str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite um valor valido')
    pessoa['idade']= int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp=str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Digite algo valido')
    if resp == 'N':
        break
print('-='*30)
print(f'AO todo temos {len(galera)} pessoa cadastradas')
media=soma/len(galera)
print(f'A medida de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}')
print()
print('Pessoas acima da media:')
for p in galera:
    if p['idade']>=media:
        for k,v in p.items():
            print(f'{k}:{v}')
        print()
print('-='*30)
print('Encerrado')