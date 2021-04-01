print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
dec = pt + (10 - 1) * razao
for c in range(pt, dec + razao, razao):
    print('{} '.format(c), end='=> ')
print('ACABOU')