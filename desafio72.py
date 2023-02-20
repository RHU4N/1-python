extN=('zero','um','dois','três','quatro','cinco','seis',
'sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis',
'dezessete','dezoito','dezenove','vinte')
while True:
    c = int(input('Digite um número de 0 a 20:'))
    if(0>c or c>20):
        print('Tente novamente.')
    else:
        break
print(f'Você digitou o número {extN[c]}')