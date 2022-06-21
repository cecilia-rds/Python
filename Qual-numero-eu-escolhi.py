from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero etre 0 e 5. Tente adivinhar')
print('Precessando...')
sleep(3)
print('-=-' * 20)
jogador = int(input('Em qual numero eu pensei?'))
if computador == jogador:
    print('Você acertou, Parabens!')
else:
    print('Eu ganhei, o numero escolhido foi {} e não {}'.format(computador, jogador))