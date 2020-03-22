valor1, valor2, valor3 = input().split(" ");
valor1 = float(valor1);
valor2 = float(valor2);
valor3 = float(valor3);
if(valor1 < valor2 + valor3 and valor2 < valor1 + valor3 and valor3 < valor1 + valor2):
    perimetro = valor1 + valor2 + valor3;
    print("Perimentro = %.1f" %perimetro);
else:
    area = valor3 * (valor1 + valor2) / 2;
    print("Area = %.1f" %area);