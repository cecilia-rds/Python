salario = float(input('Digite o salario DO funcionario R$: '))
if salario >= 1.250:
    aumento = salario + (salario*10/100)
    print('O salario será de {} com aumento de 10%'.format(aumento))
else:
    salario <= 1.200
    aumento = salario + (salario*15/100)
    print('O salario será de {} com umento de 15%'.format(aumento))