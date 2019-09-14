import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())


def dfs(s):
    # 上限を超えない範囲で再帰する
    if int(s) > n:
        return 0
    # s自身が条件を満たすか確認
    ret = 1 if all(s.count(c) > 0 for c in '357') else 0
    # 1文字増やして再帰
    for c in '357':
        ret += dfs(s + c)
    return ret


print(dfs('0'))
