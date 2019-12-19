x, a, b = map(int, input().split())
if (x + a) < b:
    print('dangerous')
elif a < b <= (x + a):
    print('safe')
else:
    print('delicious')
