n = int(input())
cnt = [0] * 30
if n % 2 == 1:
    print(0)
else:
    for i in range(30):
        cnt[i] = n // (5 ** (i + 1)) // 2
    print(sum(cnt))
