n = int(input())
v = list(map(int, input().split()))
odd = [0] * (10 ** 5 + 1)
even = [0] * (10 ** 5 + 1)
odd_cnt = []
even_cnt = []
ans = 0
for i in range(n):
    if i % 2 == 0:
        even[v[i]] += 1
    else:
        odd[v[i]] += 1
for i in range(10 ** 5 + 1):
    odd_cnt.append((odd[i], i))
    even_cnt.append((even[i], i))
even_cnt.sort(reverse=True)
odd_cnt.sort(reverse=True)
if even_cnt[0][1] == odd_cnt[0][1]:
    ans = n - max(even_cnt[0][0] + odd_cnt[1][0],
                  even_cnt[1][0] + odd_cnt[0][0])
else:
    ans = n - (even_cnt[0][0] + odd_cnt[0][0])
print(ans)
