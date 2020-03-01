a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
ans = "No"
for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                a[i][j] = -1
for i in range(3):
    if a[i][0] == a[i][1] == a[i][2] == -1:
        ans = "Yes"
for j in range(3):
    if a[0][j] == a[1][j] == a[2][j] == -1:
        ans = "Yes"
if a[0][0] == a[1][1] == a[2][2] == -1:
    ans = "Yes"
if a[0][2] == a[1][1] == a[2][0] == -1:
    ans = "Yes"
print(ans)
