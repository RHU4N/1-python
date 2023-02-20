num=list()
while True:
    n=int(input('Digite um número: '))
    num.append(n)
    print('Adicionado com sucesso')
    while True:
        c = str(input('Quer continuar?[S/N]')).upper()
        if(c=='S' or c=='N'):
            break
    if(c=='N'):
        break
print(f'Foram digitados {len(num)} numeros')
num.sort(reverse=True)
print('A ordem descresente é:')
print(num)
if(5 in num):
    print('A lista contem o valor 5')
else:
    print('A lista não contem 5')
