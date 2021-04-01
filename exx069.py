idade = 0
maioridade = 0
quanthomem = 0
mulhermenos20 = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':  # enquanto sexo não é M ou F
        sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
        pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        quanthomem += 1
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1
    if pergunta == 'N':
        break
print(f'São {maioridade} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {quanthomem} Homens.')
print(f'São {mulhermenos20} mulheres com menos de 20 anos.')
print('FIM')






