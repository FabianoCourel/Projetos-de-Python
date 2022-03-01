lista = ('APRENDER', 'PRATICAR', 'CONTAR', 'AMAR', 'COZINHAR', 'TORCER', 'CORINTHIANS')
for palavra in lista:
    print(f'\nNa palavra {palavra} temos as vogais:  ', end=' ')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=' ')