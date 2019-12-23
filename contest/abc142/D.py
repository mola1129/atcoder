import math
import fractions
a, b = map(int, input().split())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


ans = 1
divs = make_divisors(fractions.gcd(a, b))
for num in divs:
    if is_prime(num):
        ans += 1
print(ans)
