n = int(input('Qual tabuada você quer iniciar: '))
for c in range (1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))