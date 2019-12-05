n = int(input())
ans = ''
for i in range(10000):
    # 偶奇で最下位桁を決定
    if n % 2 == 0:
        ans = '0' + ans
    else:
        ans = '1' + ans
        n -= 1
    # 1ビット右シフト(-2進数)
    n //= -2
print(int(ans))
