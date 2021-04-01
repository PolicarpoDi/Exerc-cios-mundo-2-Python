
n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0: # se o numeo informado for divisivel pelo lista ele sera numero primo
        print('\033[31m', end=' ') # apresenta o numero primo com cor
        tot += 1  # conta a quantidade de numero primo informado
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mA quantidade de numero primo é {}'.format(tot))
if tot == 2:
    print('e por isso ele é primo')
else:
    print('E por isso ele não é primo')
