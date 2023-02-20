num=list()
while True:
    n=int(input('Digite um número:'))
    if n in num:
        print('Já há esse número na lista')
    else:
        num.append(n)
        print('Adicionado com sucesso')
    while True:
        c = str(input('Quer continuar?[S/N]')).upper()
        if(c=='S' or c=='N'):
            break
    if(c=='N'):
        break
num.sort()
print(num)