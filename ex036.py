print('\033[33m-=\033[m'*20)
print('         \033[31mEMPRESTIMO BANCÁRIO\033[m      ')
print('\033[33m-=\033[m'*20)
v = float(input('Digite o valor da casa: '))
s = float(input('Digite o seu salário: '))
qa = int(input('Digite a quantidade de anos: '))
a = qa * 12
pm = v / a
if pm < s - (s * 70 / 100):
    print('A parcela da casa vai ser de {:.2f}R$ em {} parcelas'.format(pm, a))
    print('Sua parcela não excedeu 30% do seu salário, então seu emprestimo foi \033[32mAPROVADO\033[m')
else:
    print('A parcela da casa vai ser de {:.2f}R$ em {} parcelas'.format(pm, a))
    print('Sua parcela excedeu 30% do seu salário, portanto o empréstimo foi \033[31mNEGADO\033[m')

