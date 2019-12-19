n = int(input())
s = [int(input()) for _ in range(n)]
candidate = [sum(s)]
for i in range(n):
    candidate.append(candidate[0] - s[i])
candidate.sort(reverse=True)
for i in range(n):
    if candidate[i] % 10 != 0:
        print(candidate[i])
        exit()
print(0)
