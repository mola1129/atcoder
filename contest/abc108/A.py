K = int(input())
even = 0
odd = 0
even = K // 2
if K % 2 == 0:
    odd = K // 2
else:
    odd = K // 2 + 1
print(even * odd)
