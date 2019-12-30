import math
x = int(input())


def is_prime(n):
    # 1は素数ではない
    if n == 1:
        return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


for i in range(x, 10 ** 6):
    if is_prime(i):
        print(i)
        exit()
