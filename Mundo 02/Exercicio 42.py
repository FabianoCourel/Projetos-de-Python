contidade = 0
contihome = 0
contimulhe = 0
print('\033[33m-=-\033[m' * 12)
print('''CADASTRE DADOS ESPECIFICOS
DE UMA PESSOA''')
print('\033[33m-=-\033[m' * 12)
while True:
    idade = int(input('Qual sua idade: '))
    if idade >= 18:
        contidade = contidade + 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Qual seu sexo? [M/F]: ').upper().strip()[0]
    if sexo == 'M':
        contihome = contihome + 1
    if sexo == 'F':
        if idade < 20:
            contimulhe = contimulhe + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if continuar == 'S':
            print('\033[33m-=-\033[m' * 12)
            print('''CADASTRE DADOS ESPECIFICOS
DE UMA PESSOA''')
            print('\033[33m-=-\033[m' * 12)
    if continuar == "N":
            break
print('\033[33m-=-\033[m' * 12)
print(f'''Pessoas com mais de 18 anos: {contidade}
Total de homens cadastrados: {contihome}
Total de mulheres com menos de 20 anos cadastradas: {contimulhe}''')
print('\033[33m-=-\033[m' * 12)
print('FIM DO REGISTRO')


