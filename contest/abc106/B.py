def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return len(divisors)


ans = 0
N = int(input())
for i in range(1, N + 1, 2):
    cnt = make_divisors(i)
    if cnt == 8:
        ans += 1
print(ans)
