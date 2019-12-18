s = input()
for i in range(1, len(s)):
    back = len(s) - i
    if back % 2 == 0 and s[:back // 2] == s[back // 2:back]:
        print(len(s[:back]))
        exit()
