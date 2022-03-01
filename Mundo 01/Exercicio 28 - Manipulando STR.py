Cidade = input(('Diga o nome de uma cidade: ')).title()
X = Cidade.split()
print('A cidade começa com o nome "Santo"? R: {}' .format('Santo' in X[0]))

print('-'*70)

Nome = input('Digite seu nome completo: ').title()
print('O nome possui "Silva" em algum lugar? R: {}' .format('Silva' in Nome.split()))