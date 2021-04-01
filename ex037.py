n = int(input('Digite um numero qualquer: '))
print('-='*20)
print('Escolha qual sera a base de conversão')
print('-='*20)
print('- 1 para\033[1;31m BINARIO\033[m')
print('- 2 para\033[1;32m OCTAL\033[m')
print('- 3 para\033[1;33m HEXADECIMAL\033[m')
escolha = int(input('Qual será a base de conversão?: '))
if escolha == 1:
    print('Você escolheu a opção {} e a conversão de {} é {} em binário'.format(escolha, n, bin(n)[2:]))
elif escolha == 2:
    print('Você escolheu a opção {} e a conversão de {} é {} em octal'.format(escolha, n, oct(n)[2:]))
elif escolha == 3:
    print('Você escolheu a opção {} e a conversão de {} é {} em Hexadecimal'.format(escolha, n, hex(n)[2:]))
else:
    print('Opção invalida, tente novamente')
