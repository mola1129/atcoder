M = input()
S = list(M)

result = "Good"
for str in S:
    if M.count(str+str) > 0:
        result = "Bad"
        break
print(result)
