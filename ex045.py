from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura') # crie a lista para informar os itens selecionados (0 ,1, 2)
computador = randint(0, 2) # o computador vai selecionar de acordo com a posição
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA \nJogue novamente')
    quit()   # faz o programa para de rodar sozinho
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('COMPUTADOR jogou {}'.format(itens[computador]))
print('JOGADOR jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE!')
