from datetime import date
data = int(input('Digite o ano de nascimento: '))
sexo = str(input('Digite o sexo: '))
ano = date.today().year
idade = ano - data
if sexo == 'Masculino':
    if idade < 18:
        print('Você tem {} anos e ainda vai se alistar ao serviço militar'.format(idade))
        falta = 18 - idade
        print('Ainda falta {} anos para você se alistar'.format(falta))
        alist = ano + falta
        print('Seu alistamento será no ano de {}'.format(alist))
    elif idade == 18:
        print('Você tem {} anos é já é hora de se alistar'.format(idade))
    elif idade > 18:
        print('Você tem {} anos, portanto já passou da faze de alistamento'.format(idade))
        fez = idade - 18
        print('Já passou {} anos da sua fase de alistamento'.format(fez))
        alist = ano - fez
        print('Foi no ano de {} que você se alistou'.format(alist))
elif sexo == 'Feminino':
    print('Você é mulher e não é obrigada a se alistar')
else:
    print('Opção invalida de sexo! Tente novamente')




