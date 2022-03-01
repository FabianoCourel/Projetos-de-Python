while True:
    print('\033[33m-=-\033[m' * 12)
    tab = int(input('Quer ver a tabuada de qual número? '))
    c = 0
    if tab < 0:
        break
    for c in range (0, 11):
        res = tab * c
        print(f'{tab} x {c} = {res}')