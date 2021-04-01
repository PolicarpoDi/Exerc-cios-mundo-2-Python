from time import sleep
print('=' * 20, 'LOJÃO DO KBÇÃO', '=' * 20)
totcompra = 0
acima1000 = 0
barato = 0
cont = 0
probarato = ' '
while True:
    produto = str(input('Digite o produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: R$'))
    cont += 1
    totcompra += preco
    if preco > 1000:
        acima1000 += 1
    if cont == 1 or preco < barato: # se contador ja estiver recebido 1 (primeira informação ele ja recebe, após isso or (OU) preco for menor que o valor em barato, ele recebe esse valor
        barato = preco
        nomebarato = produto
        probarato = produto
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        print('CALCULANDO...')
        sleep(2)
        break
print('-' * 60)
print(f'O total gasto na compra foi de R$ {totcompra:10.2f}.') # :10 é o espaço de caracteres
print(f'Foram {acima1000} comprados acima de R$ 1000,00.')
print(f'O produto mais barato foi o {probarato} que custou R$ {barato:.2f}.')