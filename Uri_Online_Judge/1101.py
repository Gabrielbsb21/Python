num1, num2 = 2, 2
aux = 0
while(num1 > 0 and num2 > 0):
    num1, num2 = input().split(" ")
    num1 = int(num1)
    num2 = int(num2)
    aux2 = num1 + 1
    if(num1 > 0 and num2 > 0):
        for i in range(num2, aux2):
            print(i , end=" ") #ends the output with a <space> 
            aux = aux + i
        print(f'Sum={aux}')
        aux = 0