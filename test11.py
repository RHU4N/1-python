print('\033[7;30;45mOlá,mundo')
a = 45
b = 43
cores = {'limpa':'\033[m', 'azul':'\033[34m'}

print('Os valores são {}{} \033[m e \033[31;41m{} \033[m'.format(cores['azul'], a,b))