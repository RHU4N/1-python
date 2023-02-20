from time import sleep
from lib.interface import *
from lib.arquivo import *

arq='cursoemvideo.txt'

if not arqExiste(arq):
    CriarArquivo(arq)


while True:
    resp=menu(['Ver cadastrados','Cadastrar novas pessoas','Sair'])
    if resp ==1:
        Lerarq(arq)
    elif resp ==2:
        cabeçalho('Novo Cadastrado')
        nome=str(input('Nome:'))
        idade=LeiaInt('Idade:')
        Cadastrar(arq,nome,idade)
    elif resp ==3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m')
    sleep(2)