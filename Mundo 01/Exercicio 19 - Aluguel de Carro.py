print('-'*70)
print('Vamos calcular os debitos do aluguel de um carro, considerando que')
print('ele custa R$60 a diaria e R$0.15 por km rodado')
print('-'*70)
n1 = float(input('Quantos KM você rodou com o carro?'))
n2 = int(input('Quantos dias você utilizou o carro?'))
km = n1*0.15
diaria = n2*60
print("Você deverá pagar R${:.2f} pelos km rodados e R${:.2f} por dias alugados. Um total de R${:.2f}". format(km, diaria, km + diaria))