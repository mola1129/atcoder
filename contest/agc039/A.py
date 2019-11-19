s = input()
k = int(input())
flag = 1
cnt = 1
ans = 0
a1 = 0
a2 = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        flag += 1
if flag == len(s):
    print(len(s) * k // 2)
    exit()

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        cnt += 1
    else:
        a1 += cnt // 2
        cnt = 1
a1 += (cnt // 2)
cnt = 1

s2 = s + s
for i in range(1, len(s2)):
    if s2[i] == s2[i - 1]:
        cnt += 1
    else:
        a2 += cnt // 2
        cnt = 1
a2 += (cnt // 2)
r = a2 - a1
print(a1 + (k - 1) * r)
