vp = float(input('Valor pago pelo produto:'))
con = int(input('Condição de pagamento \n1-dinheiro ou cheque:10% de desconto \n2-Cartão:5% de desconto \n3-Cartão 2x:preço normal \n4-3x ou mais no cartão:20% de juros \nEscolha uma opção:'))

if(con==1):
    vp = vp-(vp*(10/100))
    print('Você pagará {}'.format(vp))
elif(con==2):
    vp = vp-(vp*(5/100))
    print('Você pagará {}'.format(vp))
elif(con==3):
    vpp = vp /2
    print('v')
    print('Você pagará 2x de {} sem juro \nvc pagara R${}'.format(vpp,vp))
elif(con==4):
    vp=vp+(vp*(20/100))
    vpp = vp/3
    print('vc vai pagara 3 parcelas de {} com juros de 20%'.format(vpp))
    print('Você pagará {}'.format(vp))
else:
    print('opção invalida')

