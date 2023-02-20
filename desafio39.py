from datetime import date 
anoN = int(input('Qual ano vc nasceu:'))

idade=int(date.today().year)-anoN
print('Voce tem {}'.format(idade))

if(idade<18):
    print('Você ainda irá se alistar')
    t = 18-idade
    a = int(date.today().year) - t
    if(t==1):
        print('Falta {} ano para isso'.format(t))
        print('Seu alistamento vai ser em {}'.format(a))
    else:
        print('Falta {} anos para isso'.format(t))
        print('Seu alistamento vai ser em {}'.format(a))
elif(idade==18):
    print('Voce deve se alistar')
else:
    t=idade-18
    a = int(date.today().year) - t
    print('Voce já deveria ter se alistado há {} anos'.format(t))
    print('Seu alistamento foi em {}'.format(a))