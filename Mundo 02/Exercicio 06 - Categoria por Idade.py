from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
cat = atual - ano
if cat < 10:
    print('Com {} anos você pertence a categoria MIRIM.' .format(cat))
elif cat > 9 and cat < 15:
    print('Com {} anos você pertence a categoria INFANTIL.' .format(cat))
elif cat > 14 and cat < 20:
    print('Com {} anos você pertence a categoria JUNIOR.' .format(cat))
elif cat == 20:
    print('Com {} anos você pertence a categoria SÊNIOR.' .format(cat))
else:
    print('Acima de 21 anos você pertence a categoria MASTER')