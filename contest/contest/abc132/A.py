S = input()
s = list(S)
ans = "No"
if s[0] != s[1]:
    if S.count(s[0]) == 2 and S.count(s[1]) == 2:
        ans = "Yes"
elif s[0] != s[2]:
    if S.count(s[0]) == 2 and S.count(s[2]) == 2:
        ans = "Yes"
print(ans)
