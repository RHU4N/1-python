
while True:
    n = int(input('Qual tabuada vc quer ver:'))
    if(n<0):
        break
    print('='*20)
    for c in range(0,11):
        t = c * n
        print(f'{n:2} x {c}={t:2}')
    print('='*20)
print('Programa encerrado')

