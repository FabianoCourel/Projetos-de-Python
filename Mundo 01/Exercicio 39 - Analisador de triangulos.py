print('--=' * 20)
print('ANALISADOR DE TRIANGULOS')
print('--=' * 20)
seg1 = float(input('Primeiro seguimento: '))
seg2 = float(input('Segundo seguimento: '))
seg3 = float(input('Terceiro seguimento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os seguimentos acima PODEM formar um triangulo!')
else:
    print('Os seguimentos acima NÃO podem formar um triangulo!')