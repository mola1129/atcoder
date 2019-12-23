n = int(input())
a = set([int(input()) for _ in range(n)])
print(n - len(a))

# 別解
# n = int(input())
# a = [int(input()) for _ in range(n)]
# cnt = [0] * (10 ** 5 + 1)
# ans = 0
# for i in range(n):
#     cnt[a[i]] += 1
# for i in range(10 ** 5 + 1):
#     ans += cnt[i]
#     if cnt[i] > 0:
#         ans -= 1
# print(ans)
