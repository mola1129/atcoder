import itertools
n, m, l = map(int, input().split())
p, q, r = map(int, input().split())
package = [n, m, l]
ans = 0
for b in itertools.permutations([p, q, r]):
    tmp = 1
    for i in range(3):
        tmp *= package[i] // b[i]
    ans = max(ans, tmp)
print(ans)
