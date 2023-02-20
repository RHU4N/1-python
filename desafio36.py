vC = float(input('Qual é o valor da casa:R$'))
sC = float(input('Qual é o seu salario:R$'))
aP = int(input('Em quantos anos de finciamento:'))

pM = vC/(aP*12)
sTP = sC*(30/100)

if(pM > sTP):
    print(f'Seu salario é {sC:.2f} e a prestação é de {pM:.2f},exedendo 30% do seu salario')
    print('Emprestimo Negado')
else:
    print(f'Seu salario é {sC:.2f} e a prestação é de {pM:.2f},vc consegue pagar')
    print('Emprestimo Aprovado')