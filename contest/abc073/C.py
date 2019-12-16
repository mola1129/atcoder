import collections
n = int(input())
nums = collections.defaultdict(int)
ans = 0
for _ in range(n):
    num = int(input())
    nums[str(num)] += 1
for k in nums.keys():
    if nums[k] % 2 == 1:
        ans += 1
print(ans)
