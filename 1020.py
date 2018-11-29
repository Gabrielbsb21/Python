num = int(input());
for _ in range(num):
    num2 = int(input());
    if num2 % 2 == 0 and num2 > 0:
        print("EVEN POSITIVE");
    elif num2 % 2 == 0 and num2 < 0:
        print("EVEN NEGATIVE");
    elif num2 % 2 != 0 and num2 > 0:
        print("ODD POSITIVE");
    elif num2 % 2 !=0 and num2 < 0:
        print("ODD NEGATIVE");
    else:
        if num2 == 0:
            print("NULL");
            










































































