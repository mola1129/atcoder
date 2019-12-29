import math
txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
girls = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n):
    dst_girl = math.sqrt(
        abs(txa - girls[i][0]) ** 2 + abs(tya - girls[i][1]) ** 2)
    dst_goal = math.sqrt(
        abs(txb - girls[i][0]) ** 2 + abs(tyb - girls[i][1]) ** 2)
    dst = dst_girl + dst_goal
    if dst <= T * V:
        print('YES')
        exit()
print('NO')
