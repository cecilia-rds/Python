from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = (atual - nasc)
print('Você tem {} anos de idade'.format(idade))
if idade <= 9:
    print('Você esta na categoria MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua catego ria é JUNIOR')
elif idade <=25:
    print('Sua cateria é SENIOR')
else:
    print('Sua categoria é MASTER')