from time import sleep
import emoji
print('Iniciando a contagem regressiva.....')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[1:33mSoltaram os fogos !!!\033[m')