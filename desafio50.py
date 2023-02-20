s=0
cont=0
for c in range(0,6):
    n = int(input('Escreva um número:'))
    if(n%2==0):
        s += n
print('A soma dos numeros pares são:{}'.format(s))