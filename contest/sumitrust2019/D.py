n = int(input())
s = input()
ans = 0
password = [0, 0, 0]
for i in range(1000):
    for j in range(3):
        password[2 - j] = i // (10 ** j) % 10
    if str(password[0]) in s:
        index = s.index(str(password[0]))
        if str(password[1]) in s[index + 1:]:
            index2 = index + 1 + s[index + 1:].index(str(password[1]))
            if str(password[2]) in s[index2 + 1:]:
                ans += 1
print(ans)
