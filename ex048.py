cont = 0 # valor do contador
soma = 0 # valor do acumulador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # a soma do contador com 1 (soma +1)
        soma += c # a soma do acumulador que inicia em 0 e soma ao range (soma um valor)
print('A soma de todos os {} valores são de {}'.format(cont, soma))