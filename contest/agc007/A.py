h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
cnt = 0
for i in range(h):
    cnt += a[i].count('#')
if cnt == h + w - 1:
    print('Possible')
else:
    print('Impossible')


# 別解
# h, w = map(int, input().split())
# a = [list(input()) for _ in range(h)]


# def dfs(x, y):
#     if a[x][y] == '#':
#         a[x][y] = '.'
#     if x + 1 < h and a[x + 1][y] == '#':
#         dfs(x + 1, y)
#     elif y + 1 < w and a[x][y + 1] == '#':
#         dfs(x, y + 1)


# dfs(0, 0)
# for i in range(h):
#     for j in range(w):
#         if a[i][j] == '#':
#             print('Impossible')
#             exit()
# print('Possible')
