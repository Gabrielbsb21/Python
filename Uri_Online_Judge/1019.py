# programa feito com a versão 3.8 do Python

time = int(input())
hour = int(time / 3600)
time = time - hour * 3600
minutes = int(time / 60)
seconds = time - minutes * 60
print(f'{hour}:{minutes}:{seconds}')
