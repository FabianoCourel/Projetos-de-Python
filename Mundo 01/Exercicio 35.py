dist = float(input('Qual a distancia da viagem? '))
if dist <=200:
    v1 = dist * 0.50
    print('A passagem ira custar R$0,50 por km rodado')
else:
    v1 = dist * 0.45
    print('A passagem irá custar R$0,45 por km rodado')

print('Devido a distancia o valor da passagem será R${:.2f}' .format(v1))