media = 0
maisvelho = 0
nomevelho = ''
totm = 0
somaidade = 0
for p in range(1, 5):
    print('=' * 22)
    print('----- {}ª ----- PESSOA'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    media = somaidade / 4
    if p == 1 and sexo in 'Mm': # se for a primeira pessoa e o sexo for M ou m insere a idade e o nome
        maisvelho = idade
        nomevelho = nome
    else:
        if idade > maisvelho and sexo == 'm':
            maisvelho = idade
            nomevelho = nome
        if sexo == 'f' and idade < 20:
            totm += 1


print('A média de idade é de {}'.format(media))
print('O Homem mais velho tem {} anos e se chama {}'.format(maisvelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm))
