f=1
n = int(input('digite um número: '))
num = n
while n != 0:
    f *= n 
    n -= 1
print(f'{num}!={f}')