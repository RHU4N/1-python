num = int(input('Digite um numero de 0 a 9999:'))
u = num // 1%10
d = num // 10%10
c = num // 100%10
m= num // 1000%10

print(f'Analisando o numero {num}')

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# n= str(num)
# print(f'Analisando o numero {num}')

# print('Unidade: {}'.format(n[3]))
# print('Dezena: {}'.format(n[2]))
# print('Centena: {}'.format(n[1]))
# print('Milhar: {}'.format(n[0]))