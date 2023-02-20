# pessoas={'nome':'Gustavo','sexo':'M','idade':22}
# print(pessoas)
# print(pessoas['nome'])
# print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.values())
# print(pessoas.items())

# for k in pessoas.values():
#     print(k)

# for k,v in pessoas.items():
#     print(f'{k} = {v}')

# pessoas={'nome':'Gustavo','sexo':'M','idade':22}
# del pessoas['sexo']
# pessoas['nome']='Leandro'
# for k,v in pessoas.items():
#     print(f'{k} = {v}')

# br=list()
# estado1={'uf':'RJ','Região':'Sudeste'}
# estado2={'uf':'sp','Região':'Sudeste'}
# br.append(estado1)
# br.append(estado2)

# print(br[0]['uf'])

# estado=dict()
# brasil=list()
# for c in range(0,3):
#     estado['uf']=str(input('Unidade Federativa: '))
#     estado['sigla']=str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# for e in brasil:
#     print(e)

estado=dict()
brasil=list()
for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}.')