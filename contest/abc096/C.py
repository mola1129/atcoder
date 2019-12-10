h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            if i - 1 >= 0 and grid[i - 1][j] == '#':
                continue
            if i + 1 <= h - 1 and grid[i + 1][j] == '#':
                continue
            if j - 1 >= 0 and grid[i][j - 1] == '#':
                continue
            if j + 1 <= w - 1 and grid[i][j + 1] == '#':
                continue
            print('No')
            exit()
print('Yes')
