c=0
c1000=0
pb=0
s=0
pbs=''
while True:
    print('-'*4,c+1,'ºproduto','-'*4)
    p=str(input('Digite o nome do produto:')).strip().capitalize()
    pre=float(input('Digite o preço desse produto:'))
    i = p + ' ' + str(pre)
    info = i.split()
    print(info[0])
    print(info[1])
    s+=pre
    if(pre>1000):
        c1000+=1
    if(pb==0):
        pb=info[1]
        pbs=info[0]
    else:
        if pb>info[1]:
            pb=info[1]
            pbs=info[0]
    while True:
        con=str(input('Vc deseja continuar:[S/N]')).upper().strip()
        if(con=='S' or con=='N'):
            break
        else:
            print('Digite um dado valido')
    if(con=='N'):
        break
    c+=1
print(f'O total gasto foi R${s:.2f}')
print(f'{c1000} produtos custam mais que R$1000')
print(f'O produto mais barato é {pbs} valendo R${pb:.2f}')