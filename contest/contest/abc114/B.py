s = input()
ans = float("inf")
for i in range(len(s) - 2):
    dog = int(s[i:i + 3])
    ans = min(ans, abs(753 - dog))
print(ans)
