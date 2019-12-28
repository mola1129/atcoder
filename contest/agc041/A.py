n, a, b = map(int, input().split())
diff = abs(a - b)
if diff % 2 == 0:
    print(diff // 2)
else:
    lose = n - max(a, b)
    win = min(a, b) - 1
    print(min(win, lose) + (abs(a - b) - 1) // 2 + 1)
