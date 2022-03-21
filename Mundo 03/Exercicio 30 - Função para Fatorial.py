def factorial(n, show=False):
    """
    > Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O Valor do Fatorial do número n.
    """


    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f

print(factorial(5, show=True))
print()
help(factorial)