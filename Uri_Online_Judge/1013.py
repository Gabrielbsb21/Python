num_1, num_2, num_3 = input().split(' ')
num_1 = int(num_1)
num_2 = int(num_2)
num_3 = int(num_3)
maior_ab = int((num_1 + num_2 + abs(num_1 - num_2)) / 2)
#resultado = print(f'{maior_ab} eh o maior') if(maior_ab > num_3) else print(f'{num_3} eh o maior')
if maior_ab > num_3:
    print(f'{maior_ab} eh o maior')
else:
    print(f'{num_3} eh o maior')
