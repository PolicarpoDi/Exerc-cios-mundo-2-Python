maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o {}° peso: '.format(p)))
    if p == 1: # o primeiro range recebe o priemiro peso
        maior = peso  # portanto recebe o primeiro valor
        menor = peso  # portanto recebe o primeiro valor
    else:          # se não for o primeiro peso, começa a receber os valores
        if peso > maior:    # peso informado for maior que o peso que ja foi inserido
            maior = peso    # recebe o peso
        if peso < menor:    # peso informado for menor que o peso que ja foi inserido
            menor = peso    # recebe o peso
print('O maior peso foi de {}KG'.format(maior))
print('O menor peso foi de {}KG'.format(menor))

