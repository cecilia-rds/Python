distancia = float(input('Digite a distancia da viagem: '))
print('Você esta prestes de começar uma viagem de de {} Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(preco))