import math

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = math.pow(b, 2) - 4 * a * c

x1 = (-b + math.sqrt(delta)) / 2 * a
x2 = (-b - math.sqrt(delta)) / 2 * a

print('O valor de X1 vale {} e o valor de X2 vale {}.'.format(x1, x2))
