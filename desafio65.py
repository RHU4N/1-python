con='s'
me=0
m=0
M=0
s=0
while con=='s':
    num = int(input('Escreva um número: '))
    me+=1
    s+=num
    if(M==0 and m==0):
        M=num
        m=num
    else:
        if(num>M):
            M=num
        if(num<m):
            m=num

    con=str(input('Vc deseja continuar?[S/N]:')).lower()
media=s/me
print('A media entre todos os numeros digitado é {}'.format(media))
print('O maior número foi {}'.format(M))
print('O menor número foi {}'.format(m))
