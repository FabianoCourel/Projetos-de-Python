from uteis import cores
from uteis import interface

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        cores.vermelho('Houve um ERRO na criação do Arquivo')
    else:
        cores.verde(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        cores.vermelho('ERRO ao ler Arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        a.close()


def cadastrar(arq, nome='<Desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        cores.vermelho('ERRO ao abrir Arquivo')
    else:
       try:
           a.write(f'{nome};{idade}\n')
       except:
           cores.vermelho('ERRO ao escrever dados')
       else:
           print(f'Novo registro de {nome} cadastrado com sucesso')