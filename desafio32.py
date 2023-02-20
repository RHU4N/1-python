from datetime import date
ano = int(input('Digite seu ano atual:'))
if ano == 0:
    ano = date.today().year
if(ano%4==0 and ano %100 != 0 or ano % 400 ==0):
    print('Seu ano é bissexto')
else:
    print('Seu ano não é bissexto')