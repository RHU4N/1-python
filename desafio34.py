sal = float(input('Salario do funcionario: '))

if(sal>1250.00):
    salN = sal+(sal*(10/100))
    print('Ele recebera {}'.format(salN))
else:
    salN = sal+(sal*(15/100))
    print('Ele recebera {}'.format(salN))