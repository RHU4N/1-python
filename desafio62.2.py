p = int(input('Primeiro termo:'))
r = int(input('Qual é a razão da PA:'))
t = p
cont = 1 
total = 0
mais =10
while mais!=0:
    total = total + mais
    while cont<=total:
        print('{}-> '.format(t), end=' ')
        t+=r
        cont+=1
        print('Pausa')
        mais=int(input('Vc quer mostar mais quantos numeros:'))
print('Foram mostrados {} termos'.format(total))
    