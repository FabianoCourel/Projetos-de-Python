lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Número adicionado a lista.')
    elif n > lista[-1]:
        lista.append(n)
        print('Número adicionado a ultima posição da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos = pos + 1
print('-=-' * 30)
print(f'Os números digitados em ordem foram: {lista}')