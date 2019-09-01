import re
n = int(input())
s = [input() for _ in range(n)]
regex = r'[a-z]*(okyo)+[a-z]*(ech)+[a-z]*'
pattern = re.compile(regex)
for name in s:
    # i = str(name).find("okyo")
    # j = str(name).find("ech")
    # if i >= 0 and j >= 0 and i < j:
    #     print("Yes")
    # else:
    #     print("No")
    res = re.findall(pattern, str(name))
    if res != []:
        print("Yes")
    else:
        print("No")
