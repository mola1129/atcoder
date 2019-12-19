n = int(input())
a = [int(input()) for _ in range(n)]
pushed = [False] * n
cnt = 0
index = 0
while not (pushed[index]):
    cnt += 1
    pushed[index] = True
    if index == 1:
        cnt -= 1
        print(cnt)
        exit()
    index = a[index] - 1
print(-1)
