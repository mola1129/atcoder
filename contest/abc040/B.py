import math
n = int(input())
ans = float('inf')
for i in range(1, math.floor(math.sqrt(n)) + 1):
    j = n // i
    k = n % i
    ans = min(ans, abs(i - j) + k)
print(ans)
