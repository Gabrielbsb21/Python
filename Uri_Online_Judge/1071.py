num1 = int(input())
num2 = int(input())
soma = 0
if(num1 % 2 != 0):
    num1 -= 1
while(num1 > num2):
    if(num1 % 2 != 0):
        soma = num1 + soma
    num1 -= 1
print(soma)