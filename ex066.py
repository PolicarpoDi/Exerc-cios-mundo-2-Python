s = cont = 0
while True:
    n = int(input('Digite um número [999 para PARAR]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos valores é de {s}.')
print(f'Foram digitados {cont} números.')