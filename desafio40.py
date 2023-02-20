n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))

m = (n1+n2)/2
print('Sua media é {}'.format(m))

if(m<5):
    print('Reprovado')
elif(6.9>=m>=5):
    print('Recuperação')
elif(m>=7):
    print('Aprovado')