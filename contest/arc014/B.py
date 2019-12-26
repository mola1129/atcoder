n = int(input())
w = [input() for _ in range(n)]
kinds = set()
kinds.add(w[0])
for i in range(1, n):
    kinds.add(w[i])
    if w[i - 1][-1] != w[i][0] or len(kinds) != i + 1:
        if i % 2 == 0:
            print('LOSE')
        else:
            print('WIN')
        exit()
print('DRAW')
