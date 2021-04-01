from time import sleep

print('{:=^50}'.format(' BANCO XABLAU '))
print('-' * 50)
sacar = int(input('Qual o valor que você deseja sacar: R$'))
print('CONTANDO AS CEDÚLAS...')
sleep(5)
total = sacar # total vai receber de inicio o valor que quer sacar
cedula = 100  # a cedula inicia com 100 (no caso é a maior)
totcedula = 0
while True:   # exemplo de saque de 200 reais
    if total >= cedula:   # se o total(recebeu o valor a sacar) for maior ou igual a cedula (100)
        total -= cedula   # vai ser subtraido o valor da cedula (100) do valor a sacar (100-0)
        totcedula += 1    # vai contando +1 toda vez que retira (x2)
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        totcedula = 0
        if total == 0:
            break
print('-' * 50)
print('Volte sempre!!!')



