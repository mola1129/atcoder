n = int(input())
a = list(map(int, input().split()))
ans = 0
for num in a:
    ans += 1 / num
print(1 / ans)
