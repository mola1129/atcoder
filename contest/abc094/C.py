n = int(input())
x = list(map(int, input().split()))
x2 = sorted(x)
median_index = len(x2) // 2
median = x2[median_index]
cnt = x2.count(median_index)
for i in range(n):
    if x[i] >= median:
        print(x2[median_index - 1])
    else:
        print(x2[median_index])
