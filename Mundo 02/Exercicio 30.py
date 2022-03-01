soma = 0
media = 0
maiorhomem = 0
nomevelho = ''
mulhernova = 0
for c in range (1, 5):
    print('\033[33m-=-=-=-=-=\033[m {}ª PESSOA \033[33m-=-=-=-=-=\033[m' .format(c))
    nome = str(input('Qual o nome? '))
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual sexo? [M/F]: ')).upper().strip()
    soma = soma + idade
    if c == 1 and sexo == 'M':
        maiorhomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulhernova = mulhernova + 1

media = soma / 4
print('A media de idade do grupo é de {:.1f}' .format(media))
print('O homem mais velho se chama {} e sua idade é de {} anos!' .format(nomevelho, maiorhomem))
print('Entre as 4 pessoas há {} mulher(es) com menos de 20 anos!' .format(mulhernova))