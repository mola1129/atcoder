S = input()
cnt = 0
for i in range(0,len(S)):
    if S[i] == "o":
        cnt += 1

if  (15-len(S)) >= (8-cnt):
    print("YES")
else:
    print("NO")
