a, b = map(int, input().split())
s = input()
if len(s) == a + b + 1 and s[a] == '-':
    for i in range(len(s)):
        if i != a and not ('0' <= s[i] and s[i] <= '9'):
            print('No')
            exit()
    print('Yes')
else:
    print('No')
