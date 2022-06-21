peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = (peso / altura) ** 2
print('Seu IMC é: {:.2f}'.format(imc))
if imc < 18:
    print('Voçe está abaixo do peso ideal')
elif imc >= 18.5 <= 25:
    print('Você está no peso ideal')
elif imc == 25 <= 30:
    print('Obesidade')
else:
    print('Obesdade morbida')