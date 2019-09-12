result = 0
cnt = 0
b = list(input())
for str in b:
    if str == "A" or str == "T" or str == "C" or str == "G":
        cnt += 1
        result = max(result,cnt)
    else:
        cnt = 0
print(result)
