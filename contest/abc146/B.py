n = int(input())
s = input()
alphabet = [chr(ord('A') + i) for i in range(26)]
ans = ''

for i in s:
    for j in range(26):
        if i == alphabet[j]:
            ans += alphabet[(j + n) % 26]
print(ans)
