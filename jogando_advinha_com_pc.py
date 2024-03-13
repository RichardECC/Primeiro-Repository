#Advinhando o número que o computador está pensando, com condições e modulos 
from random import randint
from time import sleep
computador = randint(0,5)
usuario = int(input('Digite um número entre 0 e 5: '))
print('Processando.......') 
sleep(3)
print('O número que eu pensei foi {}.'.format(computador))
if usuario == computador:
    print('\033[0;30;42mEntão você ganhou!!\033[m')
else:
    print('\033[0;30;41mEntão você perdeu!!\033[m')


