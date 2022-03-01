frase = input('Digite uma frase, tente fazer um palíndromo: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]

print('Você digitou a frase {}, essa frase ao contrario fica {}!' .format(junto, inverso))
if junto == inverso:
    print('Parabéns, temos um palíndromo!')
else:
    print('Essa frase NÃO é um palíndromo!')