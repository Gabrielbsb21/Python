novo = 3;
while novo != 2:
 num = float(input());
 if num > 10 or num < 0:
    print("nota invalida");
 while num > 10 or num < 0:
    num = float(input());
    if num > 10 or num < 0:
     print("nota invalida");
 num2 = float(input());
 if num2 > 10 or num2 < 0:
    print("nota invalida");
 while num2 > 10 or num2 < 0:
    num2 = float(input());
    if num2 > 10 or num2 < 0:
     print("nota invalida");
 media = (num + num2) / 2;
 print("media = %.2f" %media);
 novo = int(input("novo calculo (1-sim 2-nao)\n"));
 if novo < 1 or novo > 2:
     novo = int(input("novo calculo (1-sim 2-nao)\n"));
     while novo < 1 or novo > 2:
         novo = int(input("novo calculo (1-sim 2-nao)\n"));
