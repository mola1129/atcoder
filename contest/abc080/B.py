n = input()
total = 0
for i in n:
    total += int(i)
if int(n) % total == 0:
    print('Yes')
else:
    print('No')
