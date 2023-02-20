t=0
c=int(input('Qual termo da PA vc deseja mostrar:'))
pt = float(input('Escreva o primeiro termo:'))
r = float(input('Escreva a razao da pa:'))

while c!=0:
    t=pt+r*c
    if(c!=0):
         print('Posição {}º dessa PA é {}'.format(c,t))
         c= int(input('Qual termo vc quer mostrar: '))
print('Obrigado por utilizar o programa')
#parte com oq foi pedido
    