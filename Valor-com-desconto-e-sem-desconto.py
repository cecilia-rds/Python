print('{:=^40}'.format(' LOJAS CECILIA '))
compra = float(input('Valor das compras: '))
pagamento = int(input('''Formas de pagamentos:
[1] À vista dinheiro/ cheque
[2] À vista cartão
[3] 2X no cartão
[4] 3X ou mais no cartão
Qual é a opção? '''))
if pagamento == 1:
    total = compra - (compra * 10 / 100)
    print(' O valor da sua compra foi R$ {:.2f} e vai custar {:.2f}'.format(compra, total))
elif pagamento == 2:
    total = compra - (compra * 5 / 100)
    print('O valor da sua compra foi {:.2f} e vai custar {:.2}'.format(compra, total))
elif pagamento == 3:
    total = compra / 2
    print('O valor a ser pago será em 2x de: {:.2f}'.format(total))
elif pagamento == 4:
    total = compra + (compra * 20 / 100)
    numparcelas = int(input('Quantas parcelas? '))
    parcelas = total / numparcelas
    print('''A compra será parcelada em {:.2f} x com juros
    Sua compra de R$ {:.2f} vai custar R$ {:.2f}
    '''.format(parcelas,compra,total))
else:
    print('Digite uma opção valida!')