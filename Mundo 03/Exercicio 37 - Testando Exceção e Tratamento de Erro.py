from uteis import cores
def leiaInt(a):
    while True:
        try:
            a = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError, KeyboardInterrupt):
            cores.vermelho('Erro! Digite corretamente o tipo do dado solicitado.')
        else:
            cores.verde('Correto!')
            break


def leiaFloat(a):
    while True:
        try:
            a = float(input('Digite um número real: ').replace(',', '.'))
        except (ValueError, TypeError, KeyboardInterrupt):
            cores.vermelho('Erro! Digite corretamente o tipo do dado solicitado.')
        else:
            cores.verde('Correto!')
            break


leiaInt(0)
leiaFloat(0)
cores.ciano('Obrigado por testar meu programa!')