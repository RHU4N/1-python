t=0
pt = float(input('Escreva o primeiro termo:'))
r = float(input('Escreva a razao da pa:'))
print('Esses sao os 10 primeiros termos dessa PA:')
for c in range(0,10):
    t=pt+r*c
    print('Posição {}º é {}'.format(c+1,t))
    
