sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]    # informar a opção
while sexo not in 'MF':   # enquanto sexo não ser M ou F
    sexo = str(input('sexo invalido... Tente novamente o valor correto: [M/F]: ')).strip().upper()[0] # uso o [0] para fatiamento, pegando a primeira letra
print('Sexo {} registrado com sucesso!'.format(sexo))
