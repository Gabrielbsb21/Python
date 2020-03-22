aux = 0
num1 = int(input())
num2 = int(input())
aux2 = num2 + 1
for i in range(num1, aux2):
    if(i % 13 != 0):
        aux = aux + i
print(aux)