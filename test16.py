lanche = ('Hamburguer','Suco','Pizza','Pudim')
# Tuplas são imutáveis
# lanche[1]='Refrigerante'
print(len(lanche))
print(lanche)
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[1:])
print(lanche[:2])
print(lanche[-3:],'\n')

for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi pra caralho \n')

for c in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posicao {c}')
print('Comi pra caralho \n')

for pos,c in enumerate(lanche):
    print(f'Eu vou comer {c}  na posicao {pos}')
print('Comi pra caralho \n')

#organizado
print(sorted(lanche))


a = (2,5,4)
b=(5,8,1,2)
c = b + a
print(c)
print(c.count(5))
print(c.index(8))
print(c.index(5,1))

pessoa = ('Rhuan',39,'M',99.88)
print(pessoa)