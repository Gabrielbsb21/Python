num1 = int(input())
num2 = int(input())
if(num1 > num2):
    for i in range(num2, num1):
        if(i % 5 == 2 or i % 5 == 3):
            print(i)
elif(num2 > num1):
    for i in range(num1, num2):
        if(i % 5 == 2 or i % 5 == 3):
            print(i)