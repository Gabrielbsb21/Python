cod,num_pec,valor = input().split(" ");
cod2,num2_pec,valor2 = input().split(" ");
cod = int(cod);
num_pec = int(num_pec);
valor = float(valor);
cod2 = int(cod2);
num2_pec = int(num2_pec);
valor2 = float(valor2);
total1 = num_pec * valor;
total2 = num2_pec * valor2;
total2 = total1 + total2;
print("VALOR A PAGAR: R$ %.2f" %total2);