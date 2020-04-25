# programa feito com a versão 3.8 do Python

nome = input()
salario = float(input())
vendas = float(input())
total = (vendas / 100) * 15 + salario
print(f'TOTAL = R$ {total:.2f}')
