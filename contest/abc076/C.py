s_dash = input()
t = input()
match_index = []
candidate = []
for i in range(len(s_dash) - len(t) + 1):
    for j in range(len(t)):
        if not(t[j] == s_dash[i + j] or s_dash[i + j] == '?'):
            break
        if j == len(t) - 1:
            match_index.append(i)
for index in match_index:
    s = s_dash[:index] + t
    if index != len(s_dash) - len(t):
        s += s_dash[index + len(t):]
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            s[i] = 'a'
    s = "".join(s)
    candidate.append(s)
candidate.sort()
if len(candidate) == 0:
    print('UNRESTORABLE')
else:
    print(candidate[0])
