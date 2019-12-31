n = int(input())
s = input()
ans = 1
for i in range(97, 97 + 26):
    ans *= s.count(chr(i)) + 1
    ans %= 10 ** 9 + 7
ans -= 1
print(ans)
