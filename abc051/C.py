sx, sy, tx, ty = map(int, input().split())
diff_x = tx - sx
diff_y = ty - sy
for _ in range(diff_x):
    print("R", end="")
for _ in range(diff_y):
    print("U", end="")
for _ in range(diff_x):
    print("L", end="")
for _ in range(diff_y):
    print("D", end="")
print("D", end="")
for _ in range(diff_x+1):
    print("R", end="")
for _ in range(diff_y+1):
    print("U", end="")
print("L", end="")
print("U", end="")
for _ in range(diff_x+1):
    print("L", end="")
for _ in range(diff_y+1):
    print("D", end="")
print("R")
