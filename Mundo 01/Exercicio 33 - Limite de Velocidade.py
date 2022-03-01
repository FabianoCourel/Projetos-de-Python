velocidade = float(input('Qual velocidade o carro está? '))
if velocidade >= 81:
    print('Você ultrapassou o limite de velocidade, está sendo multado')
    multa = (velocidade-80) * 7
    print('O valor da multa será de R${:.2f}' .format(multa))
else:
    print('Parabéns, você está dentro do limite permitido, prossiga com a viagem!')