num0 =float(input('Escreva o comprimento de uma reta: '))
num1 =float(input('Escreva o comprimento de outra reta: '))
num2 =float(input('Escreva o comprimento de outra reta: '))

if num0 < num1 + num2 and num1 < num0 + num2 and num2<num1+num0:
    print('Pode formar um triangulo')