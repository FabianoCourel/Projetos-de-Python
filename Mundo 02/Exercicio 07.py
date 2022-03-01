alt = float(input('Qual sua altura? '))
peso = float(input('Quantos KG você pesa? '))
imc = peso / alt ** 2
print('Seu IMC é: {:.2f}.' .format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <=25:
    print('Você está no seu peso ideal!')
elif imc >= 25.1 and imc <= 30:
    print('Você está com sobrepeso!')
elif imc >=30.1 and imc < 40:
    print('Você está com Obesidade')
else:
    print('Acima de 40 é considerado obesidade mórbida!')