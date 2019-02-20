num = 1
i = 0
while(num != 0):
    num = int(input())
    i = 0
    if(num != 0):
        if(num % 2 == 0):
            aux = num
            aux2 = num
            for i in range(i, 4):
                aux = aux + 2
                aux2 = aux + aux2
            print(aux2)
        elif(num % 2 != 0):
            aux = num + 1
            aux2 = num + 3
            for i in range(i, 4):
                aux = aux + 2
                aux2 = aux + aux2
            aux2 -= 2
            print(aux2)

