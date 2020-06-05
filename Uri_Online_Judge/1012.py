# programa feito com a versão 3.8 do Python
PI = 3.14159

valor_1, valor_2, valor_3 = input().split(' ')
valor_1 = float(valor_1)
valor_2 = float(valor_2)
valor_3 = float(valor_3)
triangulo = valor_1 * valor_3 / 2
circulo = valor_3 ** 2 * PI
trapezio = (valor_1 + valor_2) * valor_3 / 2
quadrado = valor_2 ** 2
retangulo = valor_1 * valor_2
print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')


