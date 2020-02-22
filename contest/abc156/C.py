n = int(input())
x = list(map(int, input().split()))
avg = round(sum(x) / n)
ans = 0
for xi in x:
    ans += (xi - avg) ** 2
print(ans)
