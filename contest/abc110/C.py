s = input()
t = input()
d = {}
for si, ti in zip(s, t):
    if si in d and d[si] != ti:
        print('No')
        exit()
    d[si] = ti
l = len(set(d.values()))
print('Yes' if len(d) == l else 'No')
