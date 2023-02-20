t=0
pt = float(input('Escreva o primeiro termo:'))
r = float(input('Escreva a razao da pa:'))
c=0
print('Esses sao os 10 primeiros termos dessa PA:')
while c!=10:
    t=pt+r*c
    c+=1
    print('Posição {}º é {}'.format(c,t))
    