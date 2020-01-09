import sys
sys.setrecursionlimit(10 ** 8)
n = int(input())
b = [[] for _ in range(n)]
for i in range(n - 1):
    b[int(input()) - 1].append(i + 1)


def dfs(v):
    if b[v] == []:
        return 1
    salary = []
    for minion in b[v]:
        salary.append(dfs(minion))
    salary.sort()
    if salary == 1:
        return 2 * salary[0] + 1
    else:
        return salary[0] + salary[-1] + 1


print(dfs(0))
