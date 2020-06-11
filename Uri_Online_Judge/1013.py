# programa feito com a versão 3.8 do Python

number_1, number_2, number_3 = input().split(' ')
number_1 = int(number_1)
number_2 = int(number_2)
number_3 = int(number_3)
maior_ab = int((number_1 + number_2 + abs(number_1 - number_2)) / 2)
#resultado = print(f'{maior_ab} eh o maior') if(maior_ab > number_3) else print(f'{number_3} eh o maior')
if maior_ab > number_3:
    print(f'{maior_ab} eh o maior')
else:
    print(f'{number_3} eh o maior')
