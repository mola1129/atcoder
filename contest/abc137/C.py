import math
n = int(input())
candidate = [sorted(list(input())) for _ in range(n)]
ans = 0
candidate.sort()


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


cnt = []
num = 1
for i in range(1, n):
    if candidate[i] == candidate[i - 1]:
        num += 1
        if i == n - 1 and num > 1:
            cnt.append(num)
    else:
        if num > 1:
            cnt.append(num)
        num = 1
for i in cnt:
    if i > 1:
        ans += combinations_count(i, 2)
print(ans)
