num = 1
i = 0 #nao eh necessario declarar a variavel i para funcionar no for, se voce quiser que o for vai do i ate algum numero, basta colocar for i in range(4) (4 por exemplo), eu acabei declarando o i, pois esqueci desse fato, e no momento de interpretar o codigo o mesmo estava apontando que a variavel i nao estava declarada. 
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

