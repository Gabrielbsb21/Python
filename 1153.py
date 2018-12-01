num = int(input());
i = num;
fat = 1;
if num == 0:
    print("0");
else:
    while i >= 1:
        fat *= i;
        i = i - 1;
print(fat);
