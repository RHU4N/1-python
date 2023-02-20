from datetime import date

ano = date.today().year
cm18=0
cM18=0

for c in range(0,7):
    anoN = int(input('Que ano vc nasceu:'))
    idade =  ano - anoN
    if(idade>=21):
        cM18+=1
    else:
        cm18+=1
print('{} são maiores de idade'.format(cM18))
print('{} são menores de idade'.format(cm18))


