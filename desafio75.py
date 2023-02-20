tupla = (int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')))
print(f'Você digitou os avlores {tupla}')
print(f'O valor nove apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1} posição')
else:
    print('Não tem 3')
print('Os valores pares são:',end='')
for n in tupla:
    if n%2==0:
        print(n,end=' ')