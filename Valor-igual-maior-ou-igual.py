num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O primeiro valor: {} é maior que o segundo: {}'.format(num1,num2))
elif num2 > num1:
    print('O segundo vaor: {} é maior que o primeiro: {}'.format(num2,num1))
else:
    print('Os vaores: são iguais'.format(num1,num2))