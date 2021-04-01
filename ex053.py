nome = str(input('Digite a frase: ')).upper().strip()
palavra = nome.split()   # gerou uma lista com o split
junto = ''.join(palavra) # o '' significa que vai juntar sem espaço e a função join vai juntar as palavras
'''inverso = ''             # vai receber uma string ''
for letra in range(len(junto) -1, -1, -1):  # fez a leitura ao inverso dela
    inverso += junto[letra]                 ##'''
inverso = junto[::-1]  # faz  a leitura por fatiamento inverso
print('O inverso de {} é {}'.format(junto,  inverso))
if inverso == junto:                        # se o invereso é a mesma coisa que o junto
    print('Temos um PALINDROMO!')
else:
    print('A frase digitada não é um PALINDROMO!')

