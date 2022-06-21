from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = (atual - nasc)
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade > 18:
    saldo = idade - 18
    print('Já passou da hora de se alistar')
    ano = idade - 18
    print('você deveria ter se alistado há {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda não é hora de se alistar, faltam {} anos'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade == 18:
    print('Você tem se alistar imediatamente')
