idade = 1
aux = 0
aux2 = 0    
while idade > 0:
    idade = int(input())
    if(idade > 0):
        aux = aux + 1
        aux2 = idade + aux2
aux = aux2 / aux
print(aux)