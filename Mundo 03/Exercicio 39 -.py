from uteis import interface, cores, dados
from time import sleep
from uteis import arquivo

arq = 'ListaExercicio39.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    interface.cabeçalho('MENU PRINCIPAL')
    interface.menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Encerrar Programa'])
    opc = dados.leiaInt('Escolha uma Opção: ')
    if opc == 1:
        interface.cabeçalho('PESSOAS CADASTRADAS')
        arquivo.lerArquivo(arq)
        sleep(2)
    elif opc == 2:
        interface.cabeçalho('CADASTRAR PESSOAS')
        try:
            nome = str(input('Nome: ')).strip()
        except nome.isnumeric():
            cores.vermelho('Dado invalido, preencha nome corretamente!')
        idade = dados.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
        sleep(2)
    elif opc == 3:
        interface.encerramento('PROGRAMA ENCERRADO', 'OBRIGADO, VOLTE SEMPRE')
        break
    else:
        cores.vermelho('Erro! Digite uma opção valida!')