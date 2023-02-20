v = float(input('Velocida do carro:'))
if(v>80):
    print('Você foi multado')
    m=(v-80)*7
    print('O valor a se pagar é {:.2f}'.format(m))
else:
    print('Dentro das normas de velocidade')