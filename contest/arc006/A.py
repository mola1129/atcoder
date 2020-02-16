e = set(map(int, input().split()))
b = int(input())
l = set(map(int, input().split()))
match = len(e & l)
if match == 6:
    print(1)
elif match == 5:
    print(2 if b in l else 3)
elif match == 4:
    print(4)
elif match == 3:
    print(5)
else:
    print(0)
