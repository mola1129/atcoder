import math
n, m = map(int, input().split())
if abs(n - m) == 0:
    print(2 * math.factorial(n) * math.factorial(m) % (10 ** 9 + 7))
elif abs(n - m) == 1:
    print(math.factorial(n) * math.factorial(m) % (10 ** 9 + 7))
else:
    print(0)
