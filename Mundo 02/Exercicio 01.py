Casa = float(input('Qual valor do imovel que deseja comprar? R$ '))
Salario = float(input('Qual valor da sua renda mensal? R$ '))
Anos = float(input('Em quantos anos pretende pagar? '))
Meses = Anos * 12
Calculo = (0.70 * Salario)
Negado = Salario - Calculo
Prest = Casa / Meses

print('O valor da prestação mensal será de R${:.2f}' .format(Prest))

if Prest >= Negado:
    print('Desculpe seu emprestimo foi \033[1;31mrecusado\033[m! O valor da prestação seria maior que 30% da sua renda.')
else:
    print('Seu emprestimo está \033[1;32maprovado\033[m, o valor da prestação será de R${:.2f}' .format(Prest))