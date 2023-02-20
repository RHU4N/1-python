def linha(tam=21):
    return '-='*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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


def menu(lista):
    cabeçalho('Menu Principal')
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m-\033[34m{item}\033[m')
        c+=1
    linha()
    opc=LeiaInt('Sua opção: ')
    return opc