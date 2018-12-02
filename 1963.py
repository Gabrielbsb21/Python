valor1,valor2 = input().split(" ");
valor1 = float(valor1);
valor2 = float(valor2);
aux = valor2 - valor1;
aux = (aux / valor1) * 100;
print("%.2f%%" %aux);
