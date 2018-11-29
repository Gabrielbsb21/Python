num1,num2,num3,num4 = input().split(" ");
num1 = int(num1);
num2 = int(num2);
num3 = int(num3);
num4 = int(num4);
soma = num3 + num4;
soma2 = num1 + num2;
if num2 > num3 and num4 > num1 and soma > soma2 and num3 > 0 and num4 > 0 and num1 %2 == 0:
    print("Valores aceitos");
else:
    print("Valores nao aceitos");
