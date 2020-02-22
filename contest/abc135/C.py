n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    # 正面の町を救う
    beaten = min(a[i], b[i])
    b[i] -= beaten
    # 隣町を救う
    beaten2 = min(a[i + 1], b[i])
    a[i + 1] -= beaten2
    ans += beaten + beaten2
print(ans)
