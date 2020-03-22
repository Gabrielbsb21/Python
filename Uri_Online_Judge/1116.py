num = int(input());
for _ in range(num):
 a,b = input().split(" ");
 a = int(a);
 b = int(b);
 if b == 0:
   print("divisao impossivel");
 else:
    div = a / b;
    print("%.1f" %div);
