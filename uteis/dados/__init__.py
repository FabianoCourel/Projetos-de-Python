from uteis import cores

def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            cores.vermelho(f'ERRO! "{entrada}" é um preço inválido!')
        else:
            return float(entrada)
            break

def leiaInt(msg):
    while True:
        try:
            opc = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            cores.vermelho('Erro! Digite corretamente o tipo do dado solicitado.')
        else:
            return opc
            break