s = 0
c = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        s = s + num
        c = c + 1
print('A soma foi : {}'.format(c, s))