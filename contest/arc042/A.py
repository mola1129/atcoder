n, m = map(int, input().split())
a = reversed([int(input()) for _ in range(m)])
f = [True] * n
for thread in a:
    if f[thread - 1]:
        print(thread)
        f[thread - 1] = False
for thread in range(n):
    if f[thread]:
        print(thread + 1)
