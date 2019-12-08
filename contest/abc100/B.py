D, N = map(int, input().split())
if D == 0:
    if N % 100 == 0:
        N += 1
    print(N)
else:
    ans = 100 ** D * N
    if ans % (100 ** (D + 1)) == 0:
        print(100 ** D * N + 100 ** D)
    else:
        print(ans)
