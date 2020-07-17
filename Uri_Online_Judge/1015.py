# programa feito com a versão 3.8 do Python

from math import sqrt
x_1, y_1 = input().split(' ')
x_2, y_2 = input().split(' ')
x_1 = float(x_1); y_1 = float(y_1); x_2 = float(x_2); y_2 = float(y_2)
result = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
print(f'{result:.4f}')
