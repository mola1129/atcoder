panel = list(map(int, input().split()))
panel.sort()
print(panel[2] * 10 + panel[1] + panel[0])
