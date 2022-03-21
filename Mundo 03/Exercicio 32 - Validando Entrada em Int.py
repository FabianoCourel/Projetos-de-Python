def leiaint(msg):
    Ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            Ok = True
        else:
            print('\033[31mErro! Digite um número inteiro.\033[m')
        if Ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')