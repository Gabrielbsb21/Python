# programa feito com a versão 3.8 do Python

cod_1, pecas_1, valor_1 = input().split(" ")
cod_2, pecas_2, valor_2 = input().split(" ")
cod_1 = int(cod_1)
pecas_1 = int(pecas_1)
valor_1 = float(valor_1)
cod_2 = int(cod_2)
pecas_2 = int(pecas_2)
valor_2 = float(valor_2)
total = pecas_1 * valor_1 + pecas_2 * valor_2
print(f'VALOR A PAGAR: R$ {total:.2f}')
