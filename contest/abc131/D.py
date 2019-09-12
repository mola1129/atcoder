N = int(input())
job = []
sum = 0
result = "Yes"
for _ in range(N):
    cost, limit = map(int, input().split())
    job.append((limit,cost))

job.sort()
for i,j in job:
    sum += j
    if i < sum:
        result = "No"
        break

print(result)
