n = int(input())
a = list(map(int, input().split()))
cnt_odd = 0
cnt_4 = 0
for i in range(n):
    if a[i] % 2 == 1:
        cnt_odd += 1
    elif a[i] % 4 == 0:
        cnt_4 += 1
if len(a) % 2 == 1 and (cnt_odd - 1) <= cnt_4:
    print('Yes')
elif len(a) % 2 == 0 and cnt_odd <= cnt_4:
    print('Yes')
else:
    print('No')
