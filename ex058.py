from time import sleep
from random import randint
print('=' * 60)
print('Vou pensar em um número e você vai tentar adivinhar........')
print('=' * 60)
sleep(2)
computador = randint(0, 10) # informa um numero aleatório de 0 a 10
acerto = 0                 # variavel para receber a quantidade de tentativas
acertou = False            # variavel que começa com False
while not acertou:         # enquanto acertou for False faça
    jogador = int(input('Em que numero eu pensei? '))
    acerto += 1
    if computador == jogador:          # se computador for igual ao jogador
        acertou = True                 # acertou recebe True, então ele para o jogo pois é diferente do False inicial
    else:
        if computador > jogador:       # se computador for maior que o jogador ele vai dizer para tentar mais para cima
            print('Mais.... tente de novo')
        elif computador < jogador:     # se computador for menor que o jogador ele vai dizer para tentar mais para baixo
            print('Menos.. tente de novo')
print('Você ACERTOU, PARABENS!!!')
print('Você tentou {} vezes para acertar!!'.format(acerto))