import datetime
Atual = datetime.date.today().year
maior = 0
menor = 0
for c in range (0, 7):
    Ano = int(input('Digite um ano de nascimento: '))
    Idade = Atual - Ano
    if Idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Você tem {} pessoas de maior idade e {} pessoas de menor idade!' .format(maior, menor))

