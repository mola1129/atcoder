import collections
n = int(input())
a = list(map(int, input().split()))
dd = collections.defaultdict(int)
correct = []
if n % 2 == 1:
    correct.append(0)
    for i in range((n - 1) // 2):
        correct.append(2 * i + 2)
        correct.append(2 * i + 2)
else:
    correct.append(1)
    correct.append(1)
    for i in range(n // 2):
        correct.append(2 * i + 3)
        correct.append(2 * i + 3)
a.sort()
correct.sort()
for i in range(n):
    if a[i] != correct[i]:
        print(0)
        exit()
for i in range(n):
    dd[str(a[i])] += 1
ans = 1
for k in dd.keys():
    if dd[k] >= 2:
        ans *= 2
        ans %= 10 ** 9 + 7
print(ans)
