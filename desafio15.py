d=int(input("Dias alugados: "))
km=float(input('Km rodados: '))

vd=60*d
vkm=0.15*km
vp=vkm+vd

print(f'O valor a se pagar com {d} dias alugados e {km}km rodados é de R${vp:.2f}')