s = input()
ans = 'Yes'
for i in range(len(s)):
    if (i + 1) % 2 != 0:
        if s[i] != 'R' and s[i] != 'U' and s[i] != 'D':
            ans = 'No'
            break
    else:
        if s[i] != 'L' and s[i] != 'U' and s[i] != 'D':
            ans = 'No'
            break
print(ans)
