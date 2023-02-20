from datetime import date
anoN = int(input('Ano de nascimento:'))
idade=int(date.today().year)-anoN
print('Voce tem {} anos \nentão vc é da categoria:'.format(idade))

if(idade<=9):
    print('Mirim')
elif(idade<=14):
    print('Infantil')
elif(idade<=19):
    print('Junior')
elif(idade<=25):
    print('Sênior')
else:
    print('master')