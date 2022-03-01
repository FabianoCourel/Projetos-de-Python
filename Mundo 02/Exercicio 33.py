from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('\033[33m-==-\033[m' * 12)
print('''[1] Somar
[2] Multiplicar
[3] Mostrar o maior
[4] Escolher novos números
[5] Sair do Programa''')
jogador = int(input('>>>> Qual a sua escolha? '))
while jogador != 5:
    if jogador == 1:
        x = n1 + n2
        print('>>> A \033[1;36mSOMA\033[m de {} e {} é: {}' .format(n1, n2, x))
        sleep(3)
        print('\033[33m-==-\033[m' * 12)
        print('''[1] Somar
[2] Multiplicar
[3] Mostrar o maior
[4] Escolher novos números
[5] Sair do Programa''')
        jogador = int(input('Qual das opções deseja realizar agora? '))
    if jogador == 2:
        x = n1 * n2
        print('>>> A \033[1;36mMULTIPLICAÇÃO\033[m de {} por {} é igual a: {}' .format(n1, n2, x))
        sleep(3)
        print('\033[33m-==-\033[m' * 12)
        print('''[1] Somar
[2] Multiplicar
[3] Mostrar o maior
[4] Escolher novos números
[5] Sair do Programa''')
        jogador = int(input('Qual das opções deseja realizar agora? '))
    if jogador == 3:
        if n1 > n2:
            print('>>> O número {} é \033[1;36mMAIOR\033[m que {}' .format(n1, n2))
            sleep(3)
            print('\033[33m-==-\033[m' * 12)
            print('''[1] Somar
[2] Multiplicar
[3] Mostrar o maior
[4] Escolher novos números
[5] Sair do Programa''')
            jogador = int(input('Qual das opções deseja realizar agora? '))
        if n1 < n2:
            print('>>> O número {} é \033[1;36mMAIOR\033[m que {}' .format(n2, n1))
            sleep(3)
            print('\033[33m-==-\033[m' * 12)
            print('''[1] Somar
[2] Multiplicar
[3] Mostrar o maior
[4] Escolher novos números
[5] Sair do Programa''')
            jogador = int(input('Qual das opções deseja realizar agora? '))
        else:
            print('>>> Ambos os valores são iguais, não há \033[1;36mMAIOR\033[m!')
            sleep(3)
            print('\033[33m-==-\033[m' * 12)
            print('''[1] Somar
[2] Multiplicar
[3] Mostrar o maior
[4] Escolher novos números
[5] Sair do Programa''')
            jogador = int(input('Qual das opções deseja realizar agora? '))
    if jogador == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print('\033[33m-==-\033[m' * 12)
        print('''[1] Somar
[2] Multiplicar
[3] Mostrar o maior
[4] Escolher novos números
[5] Sair do Programa''')
        jogador = int(input('Qual das opções deseja realizar agora? '))
    if jogador >= 6:
        jogador = int(input('Opção \033[1;31mINVALIDA\033[m, digite novamente sua opção: '))
print('\033[33m-==-\033[m' * 12)
print('Finalizando, aguarde um momento...')
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('Programa encerrado, obrigado por aguardar.')