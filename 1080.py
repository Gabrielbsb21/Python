cont = 0
maior = 0
for cont in range(1, 100):
    num = int(input())
    if(maior < num):
        maior = num
        posicao = cont
print(maior)
print(posicao)