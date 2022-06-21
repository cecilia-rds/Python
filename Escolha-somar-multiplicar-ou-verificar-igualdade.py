soma = 0
mult = 0
maior = 0
novo = 0
opção = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opção != 5:
      opção = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Qual é a sua opção? '''))
      if opção == 1:
            soma = n1 + n2
            print('A soma de {} e {} é: {}'.format(n1, n2, soma))
      elif opção == 2:
              mult = n1 * n2
              print('A multiplicação de {} e {} é: {}'.format(n1, n2, mult))
      elif opção == 3:
           if n1 > n2:
              maior = n1
              print('O maior numero entre {} e {} é: {}'.format(n1, n2, n1))
           elif n2 > n1:
              maior = n2
              print('O maior número entre  {} e {} é: {}'.format(n1.n2, n2))
           else:
               print('Os valores são iguais')
      elif opção == 4:
         n1 = int(input('''Digite novamente os valores: 
Primeiro valor: 
          '''))
         n2 = int(input('Digite o segundo valor: '))
      else:
          print('Oção invalida')
      print('=-=' * 10)
print('Fim do programa')