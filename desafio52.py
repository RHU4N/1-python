n = int(input('Escreva um número:'))
p = []
tot=0
for c in range(1,n+1):
    if(n%c==0):
        print('\033[33m', end='')
        tot+=1
    else:
        print('\033[31m', end='')
    print(' {} '.format(c), end='')

if(tot==2):
    print('\n\033[30mNumero Primo')
else:
    print('\n\033[30mO numero não é primo pois foi dividido por {}'.format(tot))