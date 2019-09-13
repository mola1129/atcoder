import numpy as np
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        res = 0
        a = np.array(x[i])
        b = np.array(x[j])
        dist = np.linalg.norm(b - a)
        if dist % 1 == 0:
            cnt += 1
print(cnt)
