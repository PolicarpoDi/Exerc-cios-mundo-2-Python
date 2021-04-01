print('-='*10)
print('    CALCULO IMC')
print('-='*10)
peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('Seu índice de massa corpórea é de {:.1f}, então você esta ABAIXO DO PESO'.format(imc))
elif imc == 18.5 or imc < 25:
    print('Seu índice de massa corpórea é de {:.1f}, então você esta no PESO IDEAL'.format(imc))
elif imc == 25 or imc < 30:
    print('Seu índice de massa corpórea é de {:.1f}, então você esta com SOBREPESO'.format(imc))
elif imc == 30 or imc < 40:
    print('Seu índice de massa corpórea é de {:.1f}, então você esta OBESO'.format(imc))
else:
    print('Seu índice de massa corpórea é de {:.1f}, então você esta com OBESIDADE MÓRBIDA'.format(imc))
