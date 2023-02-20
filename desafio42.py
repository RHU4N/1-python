num0 =float(input('Escreva o comprimento de uma reta: '))
num1 =float(input('Escreva o comprimento de outra reta: '))
num2 =float(input('Escreva o comprimento de outra reta: '))
if(num0 < num1 + num2 and num1 < num0 + num2 and num2<num1+num0):
    print('Forma um triangulo ', end='')
    if(num0==num1==num2):
        print('equilatero')
    # elif(num0==num1 and num2 < num1 + num0 or num2==num1 and num0<num1+num2 or num2 == num0 and num1 < num2+num0):
    #     print('Isosceles')
    elif(num0 != num1 != num2 != num0 ):
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Não é um triangulo')
