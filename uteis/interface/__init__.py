from uteis import dados

def cabeçalho(msg):
    print('-' * 40)
    print(f'\033[1;31m{msg.center(40)}\033[m')
    print('-' * 40)

def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c} -\033[m \033[36m{item}\033[m')
        c+=1
    print('-' * 40)

def encerramento(msg, txt):
    print('-' * 40)
    print(f'\033[1;31m{msg.center(40)}\033[m')
    print(f'\033[1;31m{txt.center(40)}\033[m')
    print('-' * 40)