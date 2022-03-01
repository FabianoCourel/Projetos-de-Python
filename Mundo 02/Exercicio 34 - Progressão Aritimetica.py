print('Gerador de PROGRESSÃO ARITIMETICA até o decimo termo')
print('\033[33m-=-\033[m' * 12)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
contador = 0
termo = primeiro
while contador < 10:
    print('{} ➔ ' .format(termo), end='')
    termo = termo + razão
    contador = contador + 1
print('FIM')