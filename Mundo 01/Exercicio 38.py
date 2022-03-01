salario = float(input('Qual valor do salario? R$'))
print('Salarios acima de R$1250,00 receberão um aumento de 10%, abaixo desse valor o aumento será de 15%')
if salario >=1250.00:
    novo = (salario * 0.10) + salario
    aumento = novo - salario
    print('Você passará a receber um total de R${:.2f}, tendo um aumento de R${:.2f}!'.format(novo, aumento))
else:
    novo = (salario * 0.15) + salario
    aumento = novo - salario
    print('Você passará a receber um total de R${:.2f}, tendo um aumento de R${:.2f}!'.format(novo, aumento))