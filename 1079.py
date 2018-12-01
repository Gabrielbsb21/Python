num = int(input());
for _ in range(num):
    a, b, c = input(). split(" ");
    a = float(a);
    b = float(b);
    c = float(c);
    media = a * 2 + b *3 + c * 5;
    media = media / 10;
    print("%.1f" %media);
    media = 0;
