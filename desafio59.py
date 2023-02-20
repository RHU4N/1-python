from time import sleep

case = 0
r=0
M=0
n1 = float(input('Escreva um número: '))
n2 = float(input('Escreva outro número: '))
while case != 5:
    print('Você deseja fazer o que:')
    case = int(input('''[1]Somar
    [2]Multiplicar
    [3]maior
    [4]Adicionar novos números
    [5]sair do programa
    Selecione sua opção:'''))
    if(case==1):
        r=n1+n2
        print(f'{n1}+{n2}={r}')
        sleep(2)
    elif(case==2):
        r=n1*n2
        print(f'{n1}*{n2}={r}')
        sleep(2)
    elif(case==3):
        if(n1>n2):
            M=n1
            print('O maior é {}'.format(M))
        elif(n2>n1):
            M=n2
            print('O maior é {}'.format(M))
        elif(n1==n2):
            print('Os dois são iguais')
        sleep(2)
    elif(case==4):
        n1 = float(input('Escreva um número: '))
        n2 = float(input('Escreva outro número: '))
        sleep(2)
    elif(case==5):
        print('Programa fechando')
        sleep(2)
    else:
        print('Isso não é uma opção valida,digite uma opção valida')
        sleep(2)






