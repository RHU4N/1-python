# def soma(a,b):
#     s=a+b
#     print('-='*5)
#     print(f'{str(s):>6}')
#     print('-='*5)

# #programa principal
# soma(4,5)
# soma(2,1)
# soma(8,9)

# def soma(a,b):
#     print(f'a={a} e b={b}')
#     s=a+b
#     print(f'{a}+{b}={s}')

# soma(3,5)

# def contador(*núm):
#     for valor in núm:
#         print(f'{valor}',end='')
#     tam=len(núm)
#     print(f'Recebi os valores {núm} que são {tam} numeros')

# contador(1,23,65,43)
# contador(1,2)

# 

def soma(*valores):
    s=0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} a soma é {s}')

soma(5,2)
soma(2,9,4)