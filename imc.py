peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
IMC = (peso / (altura*altura))

print(f'Seu IMC é {IMC:.2f}')

if IMC < 18.5:
    print('Abaixo do peso ')
elif IMC < 24.9:
    print('Peso Normal ')
elif IMC < 29.9:
    print('Sobrepeso ')
elif IMC < 39.9:
    print('Obeso ')
else:
    print('Obeso Grave ')