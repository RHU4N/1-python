import math
num = float(input('Digite um número: '))

nr = math.sqrt(num)
print('A raiz arredondada de {} é {}'.format(num,math.ceil(nr)))