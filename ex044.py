print('=-'*20)
print('         CALCULO DE VALOR PAGO')
print('=-'*20)
preco = float(input('Informe o preço do produto: '))
print('=-'*30)
print('   CONDIÇÕES DE PAGAMENTO')
print('=-'*30)
print(' - 1 À VISTA (DINHEIRO / CHEQUE - 10% de desconto')
print(' - 2 À VISTA (CARTÃO - 5% de desconto')
print(' - 3 EM ATÉ 2X NO CARTÃO (PREÇO NORMAL)')
print(' - 4 3X OU MAIS (NO CARTÃO - 20% DE JUROS')
print('=-'*30)
cond = int(input('Selecione a condição de pagamento: '))
if cond == 1:
    pa = preco - (preco * 10/100)
    print('Você selecionou a opção {} e o valor do produto vai ser de {:.2f}R$ com 10% de desconto'.format(cond, pa))
elif cond == 2:
    pa = preco - (preco * 5/100)
    print('Você selecionou a opção {} e o valor do produto vai ser de {:.2f}R$ com 5% de desconto'.format(cond, pa))
elif cond == 3:
    pa = preco / 2
    print('Você selecionou a opção {} e o valor do produto não tem desconto, porém será parcelado em 2x de {:.2f}R$'.format(cond, pa))
elif cond == 4:
    qp = int(input('Em quantas vezes você quer parcelar?: '))
    pa = preco + (preco * 20/100)
    parcelado = pa / qp
    print('Você selecionou a opção {} e o valor do produto será parcelado em {}x de {:.2f}R$, '
          'mas será acrescentado um juros de 20%, alterando o valor para {:.2f}R$'.format(cond, qp, parcelado, pa))
else:
    print('Essa condição não existe! Por favor, selecione a opção correta')