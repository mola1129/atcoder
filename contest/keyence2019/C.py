n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
plus = []
total_minus = 0
for i in range(n):
    diff = a[i] - b[i]
    if diff >= 0:
        plus.append(diff)
    else:
        total_minus += (-1) * diff
plus.sort(reverse=True)
if total_minus == 0:
    print(0)
elif sum(plus) < total_minus:
    print(-1)
else:
    ans = n - len(plus)
    for i in range(n):
        if total_minus <= 0:
            break
        total_minus -= plus[i]
        ans += 1
    print(ans)
