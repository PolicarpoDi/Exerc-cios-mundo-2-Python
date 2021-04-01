s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        s += 1  # vai somar quantos numeros pares foram informados
        cont += n # vai contando quantas vezes informou um numero
print('A quantidade de numeros pares são de {} e a soma deles é de {}'.format(s, cont))
