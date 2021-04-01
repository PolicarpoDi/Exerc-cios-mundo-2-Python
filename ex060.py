n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

'''numero = int(input('Fatorial de: '))
resultado = 1
cont = 1
for c in range(1, numero+1):
    resultado *= cont
    cont += 1
print(resultado)'''

'''from math import factorial
n = int(input('Fatoria de: '))
factorial(n)
print('O Fatorial de {} é {}'.format(n, factorial(n)))'''