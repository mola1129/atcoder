import fractions


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


n = int(input())
a = list(map(int, input().split()))
num = 1
for i in range(n):
    num = lcm(num, a[i])
ans = 0
for i in range(n):
    ans += num // a[i]
print(ans % (10 ** 9 + 7))
