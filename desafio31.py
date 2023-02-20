d = float(input('Qual é a distancia que vc viajara em km:'))

if(d<=200):
    v=d*0.50
    print('Para percorrer a distacia de {}km o valor será de R${:.2f}'.format(d,v))
else:
    v=d*0.45
    print('Para percorrer a distacia de {}km o valor será de R${:.2f}'.format(d,v))