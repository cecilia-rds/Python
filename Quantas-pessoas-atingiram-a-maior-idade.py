cont = 0
soma = 0
maior = 0
menor = 0
for c in range(1, 8):
    idade = int(input('Digite a idade da {}º pessoa: '.format(c)))
    if idade >= 21:
       maior += 1
    else:
       menor += 1
    cont += 1
print('{} pessoas atigiram a maior idade e {} são menores'. format(maior,menor))