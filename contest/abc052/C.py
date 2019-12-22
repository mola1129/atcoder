import math


def sieve_of_eratosthenes(n):
    if n == 1:
        return []
    limit = int(math.sqrt(n))
    targets = [i for i in range(2, n + 1)]
    primes = []
    while targets[0] <= limit:
        p = targets[0]
        primes.append(p)
        targets = [i for i in targets if i % p != 0]
    primes.extend(targets)
    return primes


n = int(input())
p = sieve_of_eratosthenes(n)
ans = 1
for i in p:
    cnt = 0
    for j in range(2, n + 1):
        while j % i == 0:
            j //= i
            cnt += 1
    ans *= cnt + 1
    ans %= 10 ** 9 + 7
print(ans)
