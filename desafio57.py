s = ''
while s != 'M' and s != 'F':
    s = str(input('Qual é seu sexo [M/F]: ')).upper().strip()[0]
    if s != 'M' and s != 'F':
        print('Insira o dado corretamente')
print('Sexo cdastrado com sucesso')