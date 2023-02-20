#for c in range(1, 501,2):
s = 0
cont=0
for c in range(1,500):
    if(c%2!=0 and c%3==0):
        cont = cont + 1
        s+=c
print('A soma dos {} impares de 1 a 500 que são multiplos de 3 é {}'.format(cont,s))
