import math


# エラトステネスの篩
# n以下の素数リストを返す
def sieve_of_eratosthenes(n):
    max_prime = int(math.sqrt(n))
    targets = [i for i in range(2, n + 1)]
    primes = []
    while targets[0] <= max_prime:
        p = targets[0]
        primes.append(p)
        targets = [i for i in targets if i % p != 0]
    primes.extend(targets)
    return primes
