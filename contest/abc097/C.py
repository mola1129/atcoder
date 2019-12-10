s = input()
K = int(input())
n = len(s)
substr = set()
for i in range(n):
    for j in range(i + 1, i + 1 + K):
        if j <= n:
            substr.add(s[i:j])
substr = sorted(list(substr))
print(substr[K - 1])
