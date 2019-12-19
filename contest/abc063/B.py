s = input()
present = []
for i in range(len(s)):
    if s[i] in present:
        print('no')
        exit()
    present.append(s[i])
print('yes')
