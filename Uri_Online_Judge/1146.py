num1 = 1
while num1 != 0:
    num1 = int(input())
    if(num1 != 0):
        aux = num1 + 1
        for i in range(1, aux):
            print(i, end=" ")
        print()