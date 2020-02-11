import fractions
a = int(input())
b = int(input())
n = int(input())


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


now = lcm(a, b)
ans = 0
while ans < n:
    ans += now
print(ans)
