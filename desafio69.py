c=0
ch=0
pM=0
mm20=0
while True:
    print('-'*4,c+1,'ºpessoa','-'*4)
    i=int(input('Qual sua idade:'))
    while True:
        s=int(input('''Qual é seu sexo:
        [1]Homem
        [2]mulher\nVocê é:'''))
        if(s==1 or s==2):
            break
        else:
            print('Digite um dado valido')

    if(i>=18):
        pM+=1

    if(s==1):
        ch+=1
    
    if(s==2):
        if(20>=i):
            mm20+=1


    while True:
        con=str(input('Vc deseja continuar:[S/N]')).upper().strip()
        if(con=='S' or con=='N'):
            break
        else:
            print('Digite um dado valido')
    if(con=='N'):
        break
    c+=1
print(f'{pM} pessoas tem mais de 18 anos')
print(f'{ch} homens foram cadastrados')
print(f'{mm20} mulheres tem menos de 20 anos')

