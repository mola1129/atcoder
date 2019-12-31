n = int(input())
ans = []
for _ in range(n):
    s = list(input())
    s.reverse()
    ans.append(''.join(s))
ans.sort()
for word in ans:
    word = list(word)
    word.reverse()
    print(''.join(word))
