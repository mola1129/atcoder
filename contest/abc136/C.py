n = int(input())
h = list(map(int, input().split()))
h[0] -= 1
for i in range(0, n - 1):
    diff = h[i + 1] - h[i]
    if diff >= 1:
        h[i + 1] -= 1
    elif diff < 0:
        print("No")
        exit()
print("Yes")
