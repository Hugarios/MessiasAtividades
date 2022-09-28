from math import sqrt, pow

x1 = float(input('Informe o valor de X1: '))
y1 = float(input('Informe o valor de Y1: '))
x2 = float(input('Informe o valor de X2: '))
y2 = float(input('Informe o valor de Y2: '))

distancia = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print('A distância entre os dois pontos informados é de {:.2f}.'.format(distancia))
