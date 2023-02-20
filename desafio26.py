frs = input('Digite uma frase: ').strip()

frsA = frs.lower().count('a')
frsA1 = int(frs.lower().find('a'))+1
frsAU = frs.lower().rfind('a')+1
print('A frase tem {} letras A \nO primeiro A tá na posição {} \nE o ultimo A está na posição {}'.format(frsA,frsA1,frsAU))