n = int(input())
l = list(map(int, input().split()))

l.sort()
max_num = l.pop(n - 1)
total = sum(l)
if max_num < total:
    print("Yes")
else:
    print("No")
