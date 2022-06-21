from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL     
[ 2 ] TESOURA''')
jogador = int(input(' Qual é sua jogada? '))
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if computador == 0: # Computador jogou PEdra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('OCOMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: # Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador ==2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: # Computador escolger Tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
