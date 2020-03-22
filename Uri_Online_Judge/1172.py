aux = []
b = 0
for i in range(0, 11):
    num = int(input())
    if(num < 0 or num == 0):
        aux.append(1)
    else:
        aux.append(num)
for a in range(0, 11):
    print(f'x[{b}] = {aux[a]}')
    b += 1
