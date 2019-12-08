import statistics
N = int(input())
a = list(map(int, input().split()))
for i in range(N):
    a[i] -= i + 1
# 中央値が最適
b = statistics.median(a)
# 中央値でない場合は中央値に寄せる
if b > 0 and b % 1 >= 0.5:
    b += 1
elif b < 0 and b % -1 <= -0.5:
    b -= 1
b = int(b)
ans = 0
for i in range(N):
    ans += abs(a[i] - b)
print(ans)
