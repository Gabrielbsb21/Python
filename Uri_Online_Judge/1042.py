num1, num2, num3 = input().split(" ");
num1 = int(num1);
num2 = int(num2);
num3 = int(num3);
cont1 = num1;
cont2 = num2;
cont3 = num3;
if(cont1 < cont2):
    comparador = cont1;
    cont1 = cont2;
    cont2 = comparador;
elif(cont2 < cont3):
    comparador = cont2;
    cont2 = cont3;
    cont3 = comparador;
elif(cont1 < cont2):
    comparador = cont1;
    cont1 = cont2;
    cont2 = comparador;
print("%d" %cont3);
print("%d" %cont2);
print("%d" %cont3);
print("\n");
print("%d" %num1);
print("%d" %num2);
print("%d" %num3)
