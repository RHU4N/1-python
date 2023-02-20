ig=0
hV=0
hnV= ''
cw=0
for c in range(0,4):
    print('-'*4,c+1,'ºpessoa','-'*4)
    n=str(input('Qual é seu nome:'))
    i=int(input('Qual sua idade:'))
    s=int(input('''Qual é seu sexo:
    [1]Homem
    [2]mulher\nVocê é:'''))
    ig+=i

    if(s==1):
        h = n +' '+ str(i)
        ih = h.split()
    else:
        m = n +' '+ str(i)
        im = m.split()
        if(int(im[1])<20):
            cw+=1
    
    if(c==0):
        hV=ih[1]
    else:
        if(ih[1]>hV):
            hnV=h
    info=hnV.split()

mi=ig/4
print(f'A media de idade do grupo é {mi:.2f}')
print('O homem mais velho é o {} com {} anos'.format(info[0],info[1]))
if(cw==1):
    print('Tem {} mulher com idade menor que 20 anos no grupo'.format(cw))
else:
    print('Tem {} mulheres com idade menor que 20 anos no grupo'.format(cw))