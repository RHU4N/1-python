frase = str(input('Escreva uma frase:').upper().strip())
p = frase.split()
u = "".join(p) 
inverse=u[::-1]
# inverse=''
# for l in range(len(u)-1,-1,-1):
#     inverse += u[l]

if (inverse==u):
    print(inverse)
    print('Frase é palindromo')
else:
    print(inverse)
    print('A frase não é palindromo')
