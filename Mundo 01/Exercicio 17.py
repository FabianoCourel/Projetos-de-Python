s = float(input('Qual o seu salario? R$'))
a = s + (s*0.15)
print('Se você receber um aumento de 15% seu salário de R${:.2f} passará a ser de: R$ {:.2f}' .format(s, a))