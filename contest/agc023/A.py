from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cum = [0]
for a in A:
    cum.append(cum[-1] + a)
count = Counter(cum)
ans = 0
for v in count.values():
    ans += v * (v - 1) // 2
print(ans)
