media = 0
soma = 0
maior = 0
menor = 0
cont = 0
resp = 'S'
while resp == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    cont += 1
    if maior == 0 and menor == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar?: [S/N]')).upper().strip()[0]
media = soma / cont
print('A soma entre todos os valores é de {} e a média entre todos os valores é de {:.1f}'.format(soma, media))
print('O maior número digitado foi o {}'.format(maior))
print('O menor número digitado foi o {}'.format(menor))





