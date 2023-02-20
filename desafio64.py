n=0
cont=0
s=0
while n!=999:
    n = int(input('Digite um numero [999 para parar]: '))
    if(n!=999):
        cont+=1
        s+=n
print('Vc digitou {} numeros'.format(cont))
print('A soma de todos os numeros que vc digitou foi {}'.format(s))