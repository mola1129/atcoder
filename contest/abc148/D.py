n = int(input())
a = list(map(int, input().split()))
index = float('inf')
cnt = 1
for i in range(n):
    if a[i] == 1:
        index = i
        break
if index == float('inf'):
    print(-1)
    exit()
for i in range(index, n):
    if a[i] == cnt:
        cnt += 1
cnt -= 1
print(n - cnt)
