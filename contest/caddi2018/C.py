import math
n, p = map(int, input().split())
ans = 1
for i in range(2, math.ceil(math.sqrt(p))):
    cnt = 0
    while p % i == 0 and p != 0:
        p //= i
        cnt += 1
    ans *= i ** (cnt // n)
ans *= p ** (1 // n)
print(ans)
