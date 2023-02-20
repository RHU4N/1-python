num=list()
Par=list()
impar=list()
while True:
    n=int(input('Digite um número: '))
    num.append(n)
    print('Adicionado com sucesso')
    while True:
        c = str(input('Quer continuar?[S/N]')).upper().strip()
        if(c[0]=='S' or c[0]=='N'):
            break
    if(c[0]=='N'):
        break
for c in range(0,len(num)):
    if(num[c]%2==0):
        Par.append(num[c])
    if(num[c]%2!=0):
        impar.append(num[c])
print(f'lista:{num}')
print(f'Par:{Par}')
print(f'Impar:{impar}')