a, b, k = map(int, input().split())
ans = set([])
for i in range(0, k):
    if a + i > b or b - i < a:
        break
    ans.add(a + i)
    ans.add(b - i)
ans = list(ans)
ans.sort()
for i in ans:
    print(i)
