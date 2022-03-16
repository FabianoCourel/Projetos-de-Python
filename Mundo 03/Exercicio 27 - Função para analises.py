from time import sleep
def maior(* num):
    sleep(1)
    print('\033[33m-=\033[m' * 33)
    print('Analisando os valores passados...')
    sleep(1)
    if max(num) > 0:
        for v, n in enumerate(num):
            sleep(0.4)
            print(f'{n} -', end=' ')
        sleep(1)
        print(f'Foram informados {len(num)} valores ao todo.')
        sleep(1)
        print(f'O maior valor informado foi {max(num)}.')
    else:
        sleep(1)
        print(f'Foram informados 0 valores ao todo.')
        sleep(1)
        print(f'O maior valor informado foi 0.')


maior(3, 8, 6, 7, 6, 2, 10)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)