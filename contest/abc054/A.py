a, b = map(int, input().split())
if a == 1:
    a = 100
if b == 1:
    b = 100
if a > b:
    print('Alice')
elif a < b:
    print('Bob')
else:
    print('Draw')
