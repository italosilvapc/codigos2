l1 = float(input('Digite o comprimento do primeiro lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))

if l1 == l2 == l3:
    print('Triângulo Equilátero')
if l1 != l2 != l3:
    print('Triângulo Escaleno')
else:
    print('Triângulo Isosceles')