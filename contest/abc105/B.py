n = int(input())
for cake in range(26):
    for donuts in range(15):
        if cake * 4 + donuts * 7 == n:
            print('Yes')
            exit()
print('No')
