from time import sleep
maior = 0
opcao = False
n1 = int(input('Digite o primeiro valor na tela: '))
n2 = int(input('Digite o segundo valor na tela: '))
print('-=' * 20)
while not opcao:
    sleep(1)
    print('MENU DE OPÇÕES\n'
      '[1] SOMA\n'
      '[2] MULTIPLICAR\n'
      '[3] MAIOR\n'
      '[4] NOVOS NÚMEROS\n'
      '[5] SAIR DO PROGRAMA')
    print('-=' * 20)
    selecao = int(input('SELECIONE A OPÇÃO DESEJADA:  '))
    if selecao == 1:
        print('A soma de {} + {} é igual a {}'.format(n1, n2, n1 + n2))
        print('-=' * 20)
    elif selecao == 2:
        print('A multiplicação de {} e {} é igual a {}'.format(n1, n2, n1 * n2))
        print('-=' * 20)
    elif selecao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre os numeros {} e {}, o maior é o {}'.format(n1, n2, maior))
    elif selecao == 4:
        n1 = int(input('Digite o primeiro valor na tela: '))
        n2 = int(input('Digite o segundo valor na tela: '))
        maior = 0
    elif selecao == 5:
        opcao = True
        print('Você esta saindo do programa....')
        sleep(3)
        print('Volte Sempre')
    elif selecao != [1, 5]:
        print('Opção inválida! Selecione a opção correta')

