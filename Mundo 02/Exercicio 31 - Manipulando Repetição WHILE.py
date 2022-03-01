n = input('Você é Homem ou Mulher? [M/F]: ').upper().strip()[0]
while n != 'M' and n != 'F':
    n = input('Dados inválidos. Você é Homem ou Mulher? [M/F]: ').upper().strip()[0]
print('Obrigado por responder corretamente!')
