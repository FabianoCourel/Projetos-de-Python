valor = float(input('Qual valor das compras? R$ '))
print('''FORMAS DE PAGAMENTO:
[1] A vista no dinheiro/cheque
[2] A vista no cartão
[3] 2x No cartão
[4] 3x ou mais no cartão''')
escolha = int(input('Qual opção desejada? '))

if escolha == 1:
    desc1 = valor - (valor * 0.10)
    print('A vista o valor das suas compras ficam R$ {:.2f} com 10% de desconto!' .format(desc1))
elif escolha == 2:
    desc2 = valor - (valor * 0.05)
    print('A vista no cartão o valor das suas compras ficam R$ {:.2f} com 5% de desconto!' .format(desc2))
elif escolha == 3:
    print('Em 2x no cartão parcelamos sem juros!')
elif escolha == 4:
    juros = valor + (valor * 0.20)
    parcelas = int(input('Quantas parcelas? '))
    parc = juros / parcelas
    print('''Em 3x ou mais o valor sobe com 20% de juros, ficando no total de R$ {:.2f}.
Você vai pagar {} parcelas de R$ {:.2f}''' .format(juros, parcelas, parc))
else:
    print('Opção invalida, refaça a operação!')
