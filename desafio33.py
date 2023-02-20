num0 =float(input('Escreva um numero: '))
num1 =float(input('Escreva outro numero: '))
num2 =float(input('Escreva outro número: '))

if(num0>num1 and num0>num2):
    print('O maior numero é {}'.format(num0))
if(num1>num0 and num1>num2):
    print('O maior numero é {}'.format(num1))
if(num2>num0 and num2>num1):
    print('O maior numero é {}'.format(num2))
if(num0<num1 and num0<num2):
    print('O menor numero é {}'.format(num0))
if(num1<num0 and num1<num2):
    print('O menor numero é {}'.format(num1))
if(num2<num0 and num2<num1):
    print('O menor numero é {}'.format(num2))