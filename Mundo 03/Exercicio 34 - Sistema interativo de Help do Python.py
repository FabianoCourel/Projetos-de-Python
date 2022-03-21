from time import sleep
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m')
def ajuda(com):
    titulo(f'Acessando o Manual do Comando... \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 3
    print(c[cor], end='')
    print('-' * tam)
    print(msg)
    print('-' * tam)
    sleep(1)

#Programa Principal
while True:
    titulo('   SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('    ATÉ LOGO', 1)