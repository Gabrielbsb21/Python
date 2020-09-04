# programa feito com a versão 3.8 do Python

number_1 = float(input())
if number_1 > 0 and number_1 <= 25:
    print('Intervalo [0, 25]')
elif number_1 > 25 and number_1 <= 50:
    print('Intervalo (25, 50]')
elif number_1 > 50 and number_1 <= 75:
    print('Intervalo (50, 75]')
elif number_1 > 75 and number_1 <= 100:
    print('Intervalo (75, 100]')
else:
    print('Fora do intervalo')
