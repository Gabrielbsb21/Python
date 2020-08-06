# programa feito com a versão 3.8 do Python

number_1, number_2, number_3, number_4 = input().split(' ')
number_1 = int(number_1)
number_2 = int(number_2)
number_3 = int(number_3)
number_4 = int(number_4)
sum_1 = number_3 + number_4
sum_2 = number_1 + number_2
result = "Valores aceitos" if (number_2 > number_3 and number_4 > number_1 and sum_1 >
                               sum_2 and number_3 > 0 and number_4 > 0 and number_1 % 2 == 0) else "Valores nao aceitos"

print(result)
