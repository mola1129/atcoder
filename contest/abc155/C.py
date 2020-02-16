import collections
n = int(input())
s = [input() for _ in range(n)]
s = collections.Counter(s).most_common()
ans = []
for i in range(1, len(s) + 1):
    ans.append(s[i - 1][0])
    if i == len(s):
        break
    if s[i - 1][1] != s[i][1]:
        break
ans.sort()
print(*ans, sep='\n')
