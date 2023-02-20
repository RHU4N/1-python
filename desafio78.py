num= list()
for c in range(0,5):
    num.append(int(input('Digite um numero: ')))
print(num)
for c in enumerate(num):
    str(c).split()
    if(max(num)==c[1]):
        print(f'O maior valor é {max(num)} na posição {c[0]+1}')
    if(min(num)==c[1]):
        print(f'O menor valor é {min(num)} na posição {c[0]+1}')

