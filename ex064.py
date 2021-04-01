soma = cont = n = 0  # todas as variaveis recebem o zero
while n != 999:
    n = int(input('Digite um numero inteiro [999 para \033[31mPARAR\033[m]: '))
    cont += 1
    soma += n
    if n == 999:
        print('Você parou')
        cont -= 1
        soma -= n
print('Foram digitados {} números.'.format(cont))
print('A soma de todos os números é de {}'.format(soma))

