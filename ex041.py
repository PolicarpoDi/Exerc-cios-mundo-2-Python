from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('O atleta tem {} anos. Ele faz parte da categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos. Ele faz parte da categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos. Ele faz parte da categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos. Ele faz parte da categorai SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos. Ele faz parte da categoria MASTER'.format(idade))