num1,num2,num3 = input().split(" ");
num1 = int(num1);
num2 = int(num2);
num3 = int(num3);
aux = (num1 + num2 + (abs(num1 - num2)))/2;
maior = (aux + num3 + (abs(aux - num3)))/2;
print("%d eh o maior" %maior);
