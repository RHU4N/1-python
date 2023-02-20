n=s=cont=0
while True:
    n = int(input('Digite um valor (999 faz parar):'))
    if (n==999):
        break
    cont+=1
    s+=n
print(f'Vc digitou {cont} numeros e a soma desses numeros é {s}')