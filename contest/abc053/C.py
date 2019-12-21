x = int(input())
if x % 11 == 0:
    print(x // 11 * 2)
else:
    cnt = x // 11 * 2
    x -= x // 11 * 11
    while x > 0:
        if cnt % 2 == 0:
            x -= 6
        else:
            x -= 5
        cnt += 1
    print(cnt)
