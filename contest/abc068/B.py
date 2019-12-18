n = int(input())
ans = 0
cnt = 0
while 2 ** cnt <= n:
    cnt += 1
print(2 ** (cnt - 1))
