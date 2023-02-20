# for c in range(6,0,-2):
s=0
for c in range(0,5):
    a = int(input('digite um valor:'))
    s += a
print('A soma dos valores é {}'.format(s))

n = int(input('Digite um número:'))
for c in range(0,n+1):
    print(c)
print('fim')

i = int(input('Inicio:'))
f = int(input('FIM:'))
p = int(input('Passo: '))
for c in range(i,f,p):
    print(c)
print('fim')
