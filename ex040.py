n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = float((n1 + n2) / 2)
if m < 5.0:
    print('Sua média foi de {:.1f}, portanto você esta \033[1;31mREPROVADO\033[m!'.format(m))
elif m == 5.0 or m <= 6.9:
    print('Sua média foi de {:.1f}, portanto você esta de \033[1;33mRECUPERAÇÃO\033[m!'.format(m))
elif m >= 7.0 or m <= 10:
    print('Sua média foi {:.1f}, portanto você foi \033[32mAPROVADO\033[m!'.format(m))
