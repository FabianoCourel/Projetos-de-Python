Frase = input('Digite uma frase:').lower().strip()
print('A frase possui', Frase.count('a'), 'vezes a letra "A"')
print('A primeira letra A apareceu na posição {} da frase'.format(Frase.find('a')+1))
print('A ultima letra A aparece na posição {} da frase.' .format(Frase.rfind('a')))