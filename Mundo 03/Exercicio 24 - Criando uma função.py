def area(l, c):
    area = l * c
    print(f'A área total do terreno {l} x {c} é de {area}m²')

print('<    CONTROLE DE TERRENO     >')
print('-------------------------------')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)