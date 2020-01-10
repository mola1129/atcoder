import itertools
n = int(input())
l = [i + 1 for i in range(n)]
p = list(map(int, input().split()))
q = list(map(int, input().split()))
a = 0
b = 0
cnt = 1
for v in itertools.permutations(l, n):
    for i in range(n):
        if v[i] != p[i]:
            break
        if i == n - 1:
            a = cnt
    for i in range(n):
        if v[i] != q[i]:
            break
        if i == n - 1:
            b = cnt
    cnt += 1
print(abs(a - b))
