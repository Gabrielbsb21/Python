#falta ser corrigido, programa esta pulando uma linha a mais, depois de printar os números
num1, num2 = input().split(" ")
num1 = int(num1)
num2 = int(num2)
num2 = 1 + num2
aux = 0
for i in range(1, num2):
    print(i, end=' ')
    aux += 1
    if(aux == num1):
        print("\n")
        aux = 0