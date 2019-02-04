def divisor(N):
    a = N + 1
    for i in range(1, a):
        if(N % i == 0):
            print(i)


num = int(input())
divisor(num)
