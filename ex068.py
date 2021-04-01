from random import randint
print('-' * 30)
print('Vamos jogar PAR ou IMPAR')
print('-' * 30)
v = 0
while True:  # 1 enquanto é infinito informando o que o programa pede
    n = int(input('Digite um valor: '))
    computador = randint(1, 11)
    total = n + computador
    tipo = ' '    # tipo com espaço para informar se é I - impar ou P - par
    while tipo not in 'PI': #segundo laço para saber se o tipo esta dentro do permitido, caso não, ele vai ficar perguntando
        tipo = str(input('Par ou Impar [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {n} e o computador {computador}. A soma é {total}', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR') # deu par SE o resto da divisão por 2 é 0 SENAO deu impar
    if tipo == 'P':  # se tipo for igual a P
        if total % 2 == 0:
            print('Você VENCEU')
            v += 1
        else: # senao perdeu e para
            print('Você PERDEU!')
            break
    elif tipo == 'I': #se tipo for iguala a impar voce vendeu
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else: # senao você perde e para
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!!! Você venceu {v} vezes.')


