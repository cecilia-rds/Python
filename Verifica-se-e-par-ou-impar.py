n = int(input('Digite m numero: '))
verifica = (n % 2)
if verifica == 0:
    print('O número {} é par'.format(n))
else:
    print('O numero {} é impar'.format(n))