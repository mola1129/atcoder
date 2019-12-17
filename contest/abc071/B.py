import collections
dd = collections.defaultdict(bool)
s = input()
for i in s:
    dd[i] = True
for i in range(ord('a'), ord('z') + 1):
    if not dd[chr(i)]:
        print(chr(i))
        exit()
print('None')
