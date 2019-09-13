n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
# 昇順でソート
h.sort()
ans = float("inf")
for i in range(n - k + 1):
    # 最適な選び方は、連続した並びの木k本となる
    ans = min(ans, h[i + k - 1] - h[i])
print(ans)
