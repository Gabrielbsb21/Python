def perfeito(num):
    aux = 1
    aux2 = 0
    while(aux2 < num):
            if(num % aux == 0):
                aux2 = aux + aux2
            elif(num % aux != 0):
                aux2 = aux + aux2

            aux = aux + 1
    if(aux2 == num):
        print(f'{num} eh perfeito')
    elif(aux2 != num):
        print(f'{num} nao eh perfeito')


n = int(input())
for i in range(n):
    num1 = int(input())
    perfeito(num1)
