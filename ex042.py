r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triangulo', end='')
    if r1 == r2 == r3: # o Python aceita esse tipo de declaração
        print(' EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('Não é possivel formar um triangulo com essas retas')