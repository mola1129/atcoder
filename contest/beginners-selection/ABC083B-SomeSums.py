N,A,B = map(int, input().split())
sum = 0

for i in range(1,N+1):
    digitSum = 0
    s = str(i)
    for j in range(0,len(s)):
        digitSum += int(s[j])
    if A <= digitSum <= B:
        sum += i

print(sum)
