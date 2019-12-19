import collections
s = input()
t = input()
dd = collections.defaultdict(str)
dd2 = collections.defaultdict(str)
for i in range(len(s)):
    if dd[t[i]] == '':
        dd[t[i]] = s[i]
    if dd[t[i]] != '' and dd[t[i]] != s[i]:
        print('No')
        exit()
for i in range(len(s)):
    if dd2[s[i]] == '':
        dd2[s[i]] = t[i]
    if dd2[s[i]] != '' and dd2[s[i]] != t[i]:
        print('No')
        exit()
print('Yes')
