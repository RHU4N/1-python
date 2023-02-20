nome = str(input('Seu nome completo:\n')).strip()
print('Seu nome em maiusculo {}'.format(nome.upper()))
print('Seu nome em maiusculo {}'.format(nome.lower()))

semE=int(len(nome))-int(nome.count(' '))
nomeC=nome.split()
Pn1=len(nomeC[0])


print('Seu nome completo tem {} letras'.format(semE))
print('Seu primeiro nome tem {} letras'.format(Pn1))
