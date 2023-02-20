num = int(input('Escreva um número a ser convertido:'))
con = int(input('Para qual converter \n1 = binario \n2 = octal \n3 = hexdecimal \n'))

if(con==1):
    nB=bin(num)
    print('O numero será:{}'.format(nB[2:]))
elif(con==2):
    nO =oct(num)
    print('O numero será:{}'.format(nO[2:]))
elif(con==3):
    nH = hex(num)
    print('O numero será:{}'.format(nH[2:]))
else:
    print('Opção invalida')
    



