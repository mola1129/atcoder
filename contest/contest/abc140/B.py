n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
tmp = float("inf")
ans = 0
for i in a:
    ans += b[i - 1]
    if tmp == i - 1:
        ans += c[tmp - 1]
    tmp = i
print(ans)
