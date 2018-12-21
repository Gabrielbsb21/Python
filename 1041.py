valor1, valor2 = input(). split(" "); #pega 2 valores na mesma linha e atribui a variáveis
valor1 = float(valor1);
valor2 = float(valor2);
if(valor1 > 0 and valor2 > 0):
    print("Q1");
elif(valor1 < 0 and valor2 < 0 ):
    print("Q3");
elif(valor1 > 0 and valor2 < 0):
    print("Q4");
elif(valor1 < 0 and valor > 0):
    print("Q2");
else:
    print("Origem");