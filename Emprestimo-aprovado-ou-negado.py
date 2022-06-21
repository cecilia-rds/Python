casa = float(input('Digite o valor da casa: R$'))
salario  = float(input('Digite o salario do comprador R$'))
anos = int(input('Em quando tempo o emprestimo será pago? '))
prestação = casa / (anos *12)
minimo = salario * 30 / 100
print('para pagar uma casa no valor de R${:.2f} em {} anos'.format(casa,anos), end='')
print('A prestação será de R${:2.f}'.format(prestação))
if prestação <= minimo:
    print('o Emprestimo pode ser CONCEDIDO!')
else:
    print('O emprestimo foi NEGADO!')