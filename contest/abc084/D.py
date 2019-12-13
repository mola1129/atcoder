import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


q = int(input())
scope = [tuple(map(int, input().split())) for _ in range(q)]
prime_cnt = [0] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1):
    prime_cnt[i] = prime_cnt[i - 1]
    if ((i + 1) / 2) % 1 == 0 and is_prime(i) and is_prime((i + 1) / 2):
        prime_cnt[i] += 1

for i in range(q):
    left = scope[i][0]
    right = scope[i][1]
    print(prime_cnt[right] - prime_cnt[left - 1])
