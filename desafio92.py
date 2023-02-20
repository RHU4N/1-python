from datetime import date

anoAt=date.today().year
trabalhador=dict()
trabalhador['nome']=str(input('Nome: '))
anoNasc=int(input('Que ano vc nasceu: '))
trabalhador['idade']=anoAt-anoNasc
trabalhador['cartTr']=int(input('Quanto tempo tem sua carteira de trabalho: '))
if trabalhador['cartTr']>0 and trabalhador['cartTr']!=0:
    trabalhador['anoCon']=int(input('Que ano vc foi contratado: '))
    trabalhador['salario']=float(input('Qual é o seu sálario: '))
    anoAp=anoAt+(35-trabalhador['cartTr'])
    if trabalhador['cartTr'] < 35:
        trabalhador['Aposentadadoria']=anoAp
    elif trabalhador['cartTr']>=35:
        while True:
            trabalhador['Aposentadadoria']=str(input('Com esse tempo de carteira de trabalho vc deveria ser aposentado,vc é [S/N]: ')).upper()
            if trabalhador['Aposentadadoria']=='S' or trabalhador['Aposentadadoria']=='N':
                break
            else:
                print('insira um dado valido')

        if trabalhador['Aposentadadoria']=='S':
            trabalhador['Aposentadadoria']='Aposentado'
        elif trabalhador['Aposentadadoria']=='N':
            trabalhador['Aposentadadoria']='Não é Aposentado mas pode ser'
    print(trabalhador)
else:
    print(trabalhador)
