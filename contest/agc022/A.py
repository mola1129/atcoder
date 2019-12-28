s = input()
included = set()
for i in s:
    included.add(i)
for i in range(ord('a'), ord('z') + 1):
    if not chr(i) in included:
        print(s + chr(i))
        exit()
ans = ''
for i in range(len(s) - 1, -1, -1):
    for j in range(ord(s[i]), ord('z') + 1):
        now = s[:i] + chr(j)
        if not chr(j) in s[:i] and s[:i + 1] != now:
            print(now)
            exit()
print(-1)
