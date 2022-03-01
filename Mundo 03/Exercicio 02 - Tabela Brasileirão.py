times = ('Corinthians', 'Flamengo', 'Atletico-MG', 'Palmeiras', 'Fortaleza', 'Santos',
         'Gremio', 'Cruzeiro', 'Vasco', 'Chapecoense', 'Bahia', 'São Paulo', 'Botafogo', 'Fluminense',
         'Sport', 'Internacional', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-PR')
print('\033[33m-=-\033[m' * 97)
print(f'Os times dessa edição do Brasileirão são: {sorted(times)}')
print('\033[33m-=-\033[m' * 97)
print(f'Os cinco primeiros colocados do Brasileirão são: {times[0:5]}')
print('\033[33m-=-\033[m' * 40)
print(f'Os 4 ultimos colocados do Brasileirão são: {times[-4:]}')
print('\033[33m-=-\033[m' * 31)
print(f'A chapecoense está na {len(times[13])} posição!')
print('\033[33m-=-\033[m' * 11)
