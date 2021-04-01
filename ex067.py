n = 0
while True:
    n = int(input('Digite o número para mostrar a tabuada [Digite um número negativo para PARAR]: '))
    print('-' * 40)
    if n < 0:
        print('Programa de Tabuada terminado')
        break
    for t in range(0, 11):
            print(f'{n} x {t:2} = {n * t}')
            print('-' * 15)
print('-' * 40)
