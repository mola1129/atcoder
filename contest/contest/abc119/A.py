S = input()
date = S.split('/')
ans = "Heisei"
if S != "2019/04/30" and (int(date[0]) > 2019 or int(date[1]) > 4):
    ans = "TBD"
print(ans)
