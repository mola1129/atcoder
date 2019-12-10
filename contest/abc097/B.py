X = int(input())
ans = 0
for i in range(1, 1000):
    for j in range(2, 11):
        if i ** j <= X:
            ans = max(ans, i ** j)
print(ans)
