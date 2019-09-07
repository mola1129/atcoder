n, a, b, c = map(int, input().split())
# 材料の竹
bamb = [int(input()) for _ in range(n)]
# 用意したい竹
objective = [a, b, c]
ans = float("inf")
# bit全探索
for i in range(4 ** n):
    tmp = 0
    # A,B,Cの材料となる竹のグループ分け
    material = [[] for _ in range(3)]
    # Aの材料・Bの材料・Cの材料・どの材料ともならない4パターンで探索
    for j in range(n):
        flag = (i >> (2 * j)) & 3
        if flag == 0:
            material[0].append(bamb[j])
        elif flag == 1:
            material[1].append(bamb[j])
        elif flag == 2:
            material[2].append(bamb[j])
    if len(material[0]) > 0 and len(material[1]) > 0 and len(material[2]) > 0:
        # MP計算
        for k in range(3):
            tmp += (len(material[k]) - 1) * 10
            tmp += abs(sum(material[k]) - objective[k])
        ans = min(ans, tmp)
print(ans)
