import random

a=[input('Grupo do aluno um: '),input('Grupo do aluno dois: '),input('Grupo do aluno tres: '),input('Grupo do aluno quatro: ')]

e=random.sample(a,k=4)
#e=random.shuffle(a)

print('A ordem de apresentacao é',e)