vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = float(vel/1)
    print('Você excedeu o limite de velocidade que é de 80km/h')
    multa = (vel-80) * 7
    print('Você deve pagar a multa de R$ {:.2f};'.format(multa))
print('Tenha um bom dia e dirija com segurança!')