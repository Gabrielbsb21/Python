# programa feito com a versão 3.8 do Python

total = 0
code_1, code_2 = input().split(' ')
code_1 = int(code_1)
code_2 = int(code_2)
if code_1 == 1:
    total = 4.00 * code_2
elif code_1 == 2:
    total = 4.50 * code_2
elif code_1 == 3:
    total += 5.00 * code_2
elif code_1 == 4:
    total += 2.00 * code_2
elif code_1 == 5:
    total += 1.50 * code_2

print(f'Total: R$ {total:.2f}')
