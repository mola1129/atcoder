n = int(input())
ans = 0
for i in range(1, n + 1):
    num_str = str(i)
    if len(num_str) % 2 != 0:
        ans += 1
print(ans)
