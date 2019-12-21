s = input()
index_A = float('inf')
index_Z = float('inf')
for i in range(len(s)):
    if s[i] == 'A':
        index_A = i
        break

for i in range(len(s) - 1, -1, -1):
    if s[i] == 'Z':
        index_Z = i
        break
print(len(s[index_A:index_Z + 1]))
