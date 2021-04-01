print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
total = 0
cont = 1
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} => '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais?: '))
print('Progressão finalziada com {} termos mostrados'.format(total))