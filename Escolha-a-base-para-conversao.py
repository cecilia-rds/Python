n = int(input('Digite um valor: '))
base = int(input('''Digite:
[ 1 ] para binario
[ 2 ] para octadecimal
[ 3 ] para hexadcimal'''))
if base == 1:
    convert = bin(n)[2:]
    print('O número {} convertido para binario é: {}'.format(n,convert))
elif base == 2:
    convert = oct(n)[2:]
    print(' o número {} convertido para octadecimal é: {}'. format(n,convert))
elif base == 3:
    convert = hex(n)[2:]
    print('O número {} convertido parahexadecimal é: {}'.format(n,convert))
else:
    print('Opção invalida')