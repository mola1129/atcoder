dish = []
ans = 0
for _ in range(5):
    cost = int(input())
    rest = 10 - cost % 10
    if rest == 10:
        rest = 0
    dish.append((rest, cost))

dish.sort()
for r, c in dish:
    ans += r + c
print(ans-dish[4][0])
