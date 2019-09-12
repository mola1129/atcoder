s = input()

fc = s[0]
nc = ""

count = 0

if fc == "0":
    nc = "1"
else:
    nc = "0"

for i in range(1,len(s)):
    if s[i] != nc :
        count += 1
        nc = s[i]
    else:
        if nc == "0":
            nc = "1"
        else:
            nc = "0"

print(count)
