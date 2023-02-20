pM=0
pme=0
for c in range(0,5):
    p = float(input('Qual é seu peso:'))
    if(c==0):
        pM=p
        pme=p
    else:
        if(p>pM):
            pM=p
        if(p<pme):
            pme=p


print(f'Maior:{pM}kg')
print(f'Menor:{pme}kg')
