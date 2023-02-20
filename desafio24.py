city=str(input('Digite o nome da sua cidade:')).strip()

city1 = city.split()
ton='Santo' in city1[0].capitalize()

if(ton==True):
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')