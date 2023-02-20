from datetime import date


def voto(nasc):
    if nasc<16:
        return 'Não vota'
    elif nasc>=16 and nasc<18:
        return 'vota opcionalmente'
    elif nasc>=18:
        return 'vota obrigatoriamente'
    

dataNasc=int(input('Que ano vc nasceu: '))
idade=date.today().year-dataNasc
resp=voto(idade)
print(f'Vc tem {idade} anos e {resp}')