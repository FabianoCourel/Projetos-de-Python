valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {(c)}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Você digitou os valores: {valores}')
print(f'O MAIOR número digitado foi o {maior} e sua posições na lista foram ', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end=' ')
print(f'\nO MENOR número digitado foi o {menor} e sua posição na lista foi', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end=' ')