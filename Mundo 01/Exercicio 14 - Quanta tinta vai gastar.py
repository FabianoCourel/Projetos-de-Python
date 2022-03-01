print('Vamos calcular quanta tinta vamos gastar para pintar uma parede!')
l = float(input('Qual a largura da parede?'))
a = float(input('Qual a altura da parede?'))
m2 = l*a
t = m2/2
print('Cada litro de tinta pinta 2m² de muro, nosso muro possui uma área total de', (m2),'m²')
print('Então para pintar {}m² sera gasto {}L de tinta!' .format(m2, t))