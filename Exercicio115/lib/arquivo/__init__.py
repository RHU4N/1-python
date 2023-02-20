from lib.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def CriarArquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def Lerarq(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Erro! Ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def Cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('Houve um erro para abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro para escrever o arquivo')
        else:
            print(f'Novo resgistro de {nome} adicionado')
            a.close()