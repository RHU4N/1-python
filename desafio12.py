p = float(input('Digite o preço do produto: R$'))

p5d=p-(p*(5/100))

print(f'O produto vale R${p},\nsaindo por R${p5d:.2f} com 5% de desconto')