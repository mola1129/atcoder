n = int(input())
ans = set()
limit_num = float('inf')
total = 0
for i in range(1, n + 1):
    total += i
    if total >= n:
        limit_num = i
        break
remove_num = total - n
for i in range(1, limit_num + 1):
    if i != remove_num:
        ans.add(i)
print(*ans, sep='\n')
