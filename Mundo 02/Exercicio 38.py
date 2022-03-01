cont = 0
soma = 0
while True:
    n = int(input('Digite um número, quando quiser parar digite 999: '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'A soma dos {cont} números é: {soma}!')