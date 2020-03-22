def primo(num):
    aux = 0
    aux2 = 0
    num2 = num + 1
    for i in range(1, num2):
        if(num % i == 0):
            aux = i + aux
        elif(num % i != 0):
            aux2 = i + aux2
    if(num2 == aux):
        print(f'{num} eh primo')
    elif(num2 != aux2):
        print(f'{num} nao eh primo')


n = int(input())
for i in range(n):
    x = int(input())
    primo(x)
