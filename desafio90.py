aluno=dict()
aluno['nome']=str(input('Nome do aluno: '))
aluno['média']=float(input(f'Média do {aluno["nome"]}: '))
if aluno['média']>=7:
    aluno['situação']='aprovado'
elif aluno['média']<7 and aluno['média']>=5:
    aluno['situação']='recuperação'
else:
    aluno['situação']='reprovado'
for k,v in aluno.items():
    print(f'{k}:{v}')