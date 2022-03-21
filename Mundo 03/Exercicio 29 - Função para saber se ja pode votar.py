def voto(a=0):
    from datetime import date
    ano = date.today().year
    i = ano - a
    if i < 16:
        return f'Com {i} anos: \033[31mNAO VOTA\033[m'
    elif 16 <= i < 18 or i >= 65:
        return f'Com {i} anos: VOTO \033[33mOPCIONAL\033[m'
    else:
        return f'Com {i} anos: VOTO \033[32mOBRIGATORIO\033[m'


nasc = int(input('Ano você nasceu: '))
print(voto(nasc))