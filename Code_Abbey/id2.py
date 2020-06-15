numbers = []
n = int(input())
for i in range(n):
    numbers = input().split(' ')
    if len(numbers) == n:
        break

numbers = list(map(int, numbers))
result = sum(numbers)
print(result)
