nome = str(input('Qual seu nome: '))
if nome == 'Rhuan':
    print('Que nome bonito')
elif nome == 'Valentina' or nome == 'Enzo':
    print('Seu nome é bem comum')
elif nome in 'Ana Claudia Jessica Juliana':
    print('É um nome geralmente feminino')
else:
    print('Que nome normal')

print('Tenha um bom dia {}'.format(nome))