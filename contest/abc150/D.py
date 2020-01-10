import fractions


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


# 2で割れる回数を数える
def f(x):
    t = 0
    while (x % 2 == 0):
        x //= 2
        t += 1
    return t


n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] //= 2

cnt = f(a[0])
for i in range(n):
    # 割れる回数が一致しなければ不可
    if cnt != f(a[i]):
        print(0)
        exit()
    a[i] >>= cnt
m >>= cnt
num = 1
for i in range(n):
    num = lcm(num, a[i])
    if num > m:
        print(0)
        exit()
m //= num
ans = (m + 1) // 2
print(ans)
