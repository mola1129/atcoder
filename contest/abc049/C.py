s = list(input())
t = ''
cnt = len(s) - 1
while cnt >= 0:
    if s[cnt] == 'm':
        t = 'dream' + t
        cnt -= 5
        continue
    if s[cnt] == 'e':
        t = 'erase' + t
        cnt -= 5
        continue
    if s[cnt] == 'r':
        if cnt - 2 >= 0 and s[cnt - 2] == 'm':
            t = 'dreamer' + t
            cnt -= 7
            continue
        elif cnt - 2 >= 0 and s[cnt - 2] == 's':
            t = 'eraser' + t
            cnt -= 6
            continue
    break
s = ''.join(s)
if s == t:
    print('YES')
else:
    print('NO')
