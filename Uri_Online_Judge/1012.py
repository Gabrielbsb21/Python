# programa feito com a versão 3.8 do Python
PI = 3.14159

value_1, value_2, value_3 = input().split(' ')
value_1 = float(value_1); value_2 = float(value_2); value_3 = float(value_3)
triangle = value_1 * value_3 / 2
circle = value_3 ** 2 * PI
trapezium = (value_1 + value_2) * value_3 / 2
square = value_2 ** 2
rectangle = value_1 * value_2
print(f'TRIANGULO: {triangle:.3f}')
print(f'CIRCULO: {circle:.3f}')
print(f'TRAPEZIO: {trapezium:.3f}')
print(f'QUADRADO: {square:.3f}')
print(f'RETANGULO: {rectangle:.3f}')
