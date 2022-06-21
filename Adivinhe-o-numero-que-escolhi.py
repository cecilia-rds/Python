from random import randint
from time import sleep
computador = randint(0, 5)
c = 1
print('Vou pensar em um numero entre 0 e 5, Tente adivinhar: ')
jogador = int(input('Qual eu escolhi? '))
print(computador)
while computador != jogador:
    jogador = int(input('Você errou, tente novamente {}'.format(c)))
    c += 1
else:
    print('Você acertou, foram necessarias {} tentativas'.format(c))