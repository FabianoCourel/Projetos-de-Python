from uteis import cores

def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            cores.vermelho(f'ERRO! "{entrada}" é um preço inválido!')
        else:
            return float(entrada)
            break
