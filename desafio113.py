def LeiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print('\033[31mDigite um dado valido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mEntrada de dados interropida pelo usuario\033[m')
            return 0
        else:
            return n
        

def LeiaFloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError,TypeError):
            print('\033[31mDigite um dado valido\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mEntrada de dados interropida pelo usuario\033[m')
            return 0
        else:
            return n


num1 = LeiaInt('Digite um valor: ')
num2 = LeiaFloat('Digite um valor: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')