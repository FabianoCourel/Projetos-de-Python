from uteis import moeda, cores
from time import sleep

cores.amarelo('-=' * 13)
valor = float(input('Digite um valor: R$ '))
cores.amarelo('-=' * 30)
sleep(1)
cores.ciano(f'Aumentando em 10% o valor de {moeda.moeda(valor)} temos: {moeda.mais(v = valor, p = 10, formato=True)}')
sleep(1)
cores.ciano(f'Diminuindo em 10% o valor de {moeda.moeda(valor)} temos: {moeda.menos(valor, 10, True)}')
sleep(1)
cores.ciano(f'Dobrando o valor de {moeda.moeda(valor)} temos: {moeda.dobro(valor, True)}')
sleep(1)
cores.ciano(f'Metade de {moeda.moeda(valor)} é: {moeda.metade(valor, True)}')
sleep(1)
cores.amarelo('-=' * 30)
cores.vermelho('Encerrando programa...')
sleep(1)
cores.vermelho('    FIM do Teste.')
