n = int(input())
ans = []
flag = False
for i in range(4 ** n):
    s = ''
    for j in range(n):
        if ((i >> 2 * j) & 3) == 0:
            s += 'a'
        elif ((i >> 2 * j) & 3) == 1:
            s += 'b'
        elif ((i >> 2 * j) & 3) == 2:
            s += 'c'
        else:
            flag = True
            break
    if flag:
        flag = False
        continue
    ans.append(s)
ans.sort()
for i in range(len(ans)):
    print(ans[i])
