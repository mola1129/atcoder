n = int(input())
for i in range(10 ** 5, 0, -1):
    num = i ** 2
    if num <= n:
        print(num)
        exit()
