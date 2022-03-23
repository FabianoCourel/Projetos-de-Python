from time import sleep

def mais(v = 0, p = 0, formato=False):
    porc = (v / 100) * p
    res = v + porc
    return res if formato is False else moeda(res)


def menos(v = 0, p = 0, formato=False):
    porc = (v / 100) * p
    res = v - porc
    return res if formato is False else moeda(res)


def metade(v = 0, formato=False):
    res = v - (v / 2)
    return res if formato is False else moeda(res)


def dobro(v = 0, formato=False):
    res = v + v
    return res if formato is False else moeda(res)


def moeda(v = 0, moeda = 'R$ '):
    return f'{moeda}{v:.2f}'.replace('.', ',')

def resumo(a=0, b=0, c=0):
    print('-' * 32)
    print('RESUMO DO VALOR'.center(32))
    print('-' * 32)
    sleep(2)
    print(f"Preço Analisado \t{moeda(a)}")
    print(f'Dobro do Preço  \t{dobro(a, True)}')
    print(f'Metade do Preço \t{metade(a, True)}')
    print(f'{b}% de Aumento  \t{mais(a, b, True)}')
    print(f'{c}% de Redução  \t{menos(a, c, True)}')
    print('-' * 32)