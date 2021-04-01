print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
pa = 0
cont = 1
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termo = pt
while cont <= 10:
    print('{} => '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')