n = int(input())
s = input()
bcnt = [0]*n
wcnt = [0]*n
result = 2 * 10 ** 5

# 累積和
if s[0] == "#":
    bcnt[0] = 1
if s[n-1] == ".":
    wcnt[n-1] = 1

for i in range(1,n):
    bcnt[i] = bcnt[i-1]
    if s[i] == "#":
        bcnt[i] += 1
for i in range(n-2,-1,-1):
    wcnt[i] = wcnt[i+1]
    if s[i] == ".":
        wcnt[i] += 1

# 最小コストを求める
for i in range(0,n-1):
    result = min(bcnt[i] + wcnt[i+1],result)

result = min(result,bcnt[n-1])
result = min(result,wcnt[0])

print(result)
