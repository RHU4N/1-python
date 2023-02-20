n = int(input('Escolha um número:'))
print('='*12)
for c in range(0,11):
    t = c * n
    print(f'{c:2}x{n}={t:2}')
print('='*12)