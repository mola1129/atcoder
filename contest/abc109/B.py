from collections import defaultdict
# 辞書型の利用
dd = defaultdict(bool)
n = int(input())
w = [input() for _ in range(n)]
pre = w[0][0]
for s in w:
    # 既に出ている or  しりとりの連結が適切でない
    if dd[s] or (pre[len(pre) - 1] != s[0]):
        print("No")
        exit()
    # その出現したワードを記憶
    dd[s] = True
    pre = s
print("Yes")
