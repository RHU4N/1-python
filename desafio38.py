num0 = int(input('Digite um numero:'))
num1 = int(input('Digite outro numero:'))

if(num0>num1):
    nM = num0
    nm = num1
    print(f'O Numero maior é {nM} \ne o menor é {nm}')
elif(num1>num0):
    nM = num1
    nm = num0
    print(f'O Numero maior é {nM} \ne o menor é {nm}')
else:
    print('Os dois numeros sao iguais e não há maior ou menor')

