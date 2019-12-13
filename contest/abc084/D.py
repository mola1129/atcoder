import math
q = int(input())
scope = [tuple(map(int, input().split())) for _ in range(q)]
prime_flag = [True] * (10 ** 5 + 1)
prime_flag[0] = False
prime_flag[1] = False
prime_cnt = [0] * (10 ** 5 + 1)

# エラトステネスの篩
# 愚直解でも通った
for i in range(2, math.ceil(math.sqrt(10 ** 5))):
    for j in range(i + i, 10 ** 5 + 1, i):
        prime_flag[j] = False


for i in range(2, 10 ** 5 + 1):
    prime_cnt[i] = prime_cnt[i - 1]
    num = (i + 1) / 2
    if num % 1 == 0 and prime_flag[i] and prime_flag[int(num)]:
        prime_cnt[i] += 1

for i in range(q):
    left = scope[i][0]
    right = scope[i][1]
    print(prime_cnt[right] - prime_cnt[left - 1])
