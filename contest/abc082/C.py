import collections
n = int(input())
a = list(map(int, input().split()))
dd = collections.defaultdict(int)
ans = 0
for i in range(n):
    dd[str(a[i])] += 1
for k in dd.keys():
    v = dd[k]
    diff = int(k) - v
    if diff <= 0:
        ans += abs(diff)
    else:
        ans += v
print(ans)

# 別解
# a.sort()
# a.append(0)
# num = a[0]
# cnt = 1
# ans = 0
# for i in range(1, n + 1):
#     if a[i] == num:
#         cnt += 1
#     else:
#         diff = num - cnt
#         if diff <= 0:
#             ans += abs(diff)
#         else:
#             ans += cnt
#         num = a[i]
#         cnt = 1
# print(ans)
