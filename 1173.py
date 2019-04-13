lista = []
a = 0
num = int(input())
for i in range(10):
    lista.append(num)
    num = num * 2
for i in range(10):
    print(f'N[{a}]= {lista[i]}', end="\n")
    a = a + 1


