h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            cnt = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if 0 <= i + k and 0 <= j + l and i + k < h and j + l < w and s[i + k][j + l] == '#':
                        cnt += 1
            s[i][j] = cnt
for i in range(h):
    print(*s[i], sep='')
