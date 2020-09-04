# programa feito com a versão 3.8 do Python
import math
number_1, number_2, number_3 = input().split(' ')
number_1 = float(number_1)
number_2 = float(number_2)
number_3 = float(number_3)
delta = number_2 ** 2 - 4 * number_1 * number_3
if delta < 0:
    print("Impossivel calcular")
else:
    delta = math.sqrt(delta)
    square_root_1 = (-number_2 + delta) / (2 * number_1)
    square_root_2 = (-number_2 - delta) / (2 * number_1)

print(square_root_1)
print(square_root_2)
