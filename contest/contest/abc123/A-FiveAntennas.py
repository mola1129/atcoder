a = []
sum = 0
for i in range(6):
    a.append(int(input()))
dist = a[4] - a[0]
if dist > a[5]:
    print(":(")
else:
    print("Yay!")
