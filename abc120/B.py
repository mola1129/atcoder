a, b, k = map(int, input().split())
candidate = []
for div in range(1, min(a, b) + 1):
    if a % div == 0 and b % div == 0:
        candidate.append(div)
candidate.sort()
candidate.reverse()
print(candidate[k-1])
