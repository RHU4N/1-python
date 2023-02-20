num0 =float(input('Escreva o comprimento de uma reta: '))
num1 =float(input('Escreva o comprimento de outra reta: '))
num2 =float(input('Escreva o comprimento de outra reta: '))

if(num0**2==num1**2+num2**2 or num1**2==num0**2+num2**2 or num2**2==num1**2+num0**2):
    print('É possivel forma um triangulo retangulo')
else:
    print('Não é possivel forma um triangulo retangulo')