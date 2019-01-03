num = int(input())
x = 0
t = 0
for i in range(0 , num):
    num2 = int(input())
    if(num2 >= 10 and num2 <= 20):
        x += 1
    elif(num2 < 10 or num2 > 10):
        t += 1
print("%d in" %x)
print("%d out" %t)
