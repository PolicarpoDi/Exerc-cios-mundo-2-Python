from datetime import date
d = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    a = int(input('Em que ano a {}° pessoa nasceu?: '.format(c)))
    idade = d - a
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print('Existe {} pessoas menores de idade'.format(menor))
print('Existe {} pessoas maiores de idade'.format(maior))
