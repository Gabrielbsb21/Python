# programa feito com a versão 3.8 do Python

code_1, product_1, price_1 = input().split(" ")
code_2, product_2, price_2 = input().split(" ")
code_1 = int(code_1)
product_1 = int(product_1)
price_1 = float(price_1)
code_2 = int(code_2)
product_2 = int(product_2)
price_2 = float(price_2)
total = product_1 * price_1 + product_2 * price_2
print(f'VALOR A PAGAR: R$ {total:.2f}')
