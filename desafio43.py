p = float(input('Qual é seu peso:'))
a = float(input('Qual é sua altura:'))

imc = p/(a*a)

print('seu imc é ',imc)

if(imc<18.5):
    print('Abaixo do peso')
elif(25>imc>=18.5):
    print('Peso ideal')
elif(25 <= imc < 30 ):
    print('Sobrepeso')
elif(30<=imc and imc<40):
    print('Obesidade')
elif(imc>=40):
    print('Obesidade morbida')