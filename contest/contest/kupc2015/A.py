t = int(input())
s = [input() for _ in range(t)]
ans = []
for testcase in s:
    cnt = 0
    while True:
        # はじめにでてくるtokyo or kyotoの位置を算出
        index_t = testcase.find("tokyo")
        index_k = testcase.find("kyoto")
        index = float("inf")
        if index_k >= 0 and index_t >= 0:
            # どっちもあるなら、早い方を採用
            index = min(index_k, index_t)
        elif index_k * index_t <= 0:
            index = max(index_k, index_t)
        else:
            # 無いなら終了
            ans.append(cnt)
            break
        if index != float("inf"):
            # 切り取って再スタート
            testcase = testcase[index + 5:]
            cnt += 1
for res in ans:
    print(res)
