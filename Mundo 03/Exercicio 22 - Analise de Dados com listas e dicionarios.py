dados = {}
lista = []
mulheres = []
tot = 0
idade = 0
media = 0
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    while True:
        tot = tot+1
        dados['Sexo'] = str(input('Digite o sexo [M/F/O]: ')).upper().strip()[0]
        if dados['Sexo'] in 'MFO':
            if dados['Sexo'] == 'F':
                mulheres.append(dados['Nome'])
            break
        print('Resposta \033[31mINVALIDA\033[m! Por favor digite corretamente.')
    dados['Idade'] = int(input('Digite a idade: '))
    idade = (dados['Idade'] + idade)
    media = idade / tot
    lista.append(dados.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if continuar in "SN":
            print('-' * 60)
            break
        elif continuar not in 'SN':
            print('Resposta \033[31mINVALIDA\033[m! Por favor digite corretamente.')
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {tot} pessoas cadastradas!')
print(f'B) A media de idade delas é de {media:2f} anos!')
print(f'C) As mulheres cadastradas foram: {mulheres}')
print('D) Lista de pessoas que estão acima da media de idade:')
for p in lista:
    if p['Idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'    > {k:} = {v:}; ', end='')
        print('')
print('\n<< ENCERRADO >>')

