from operator import itemgetter
n = int(input())
red = [tuple(map(int, input().split())) for _ in range(n)]
blue = [tuple(map(int, input().split())) for _ in range(n)]
red.sort(key=itemgetter(1), reverse=True)
blue.sort()
red_flag = [False] * n
for i in range(n):
    pair_red_index = float('inf')
    for j in range(n):
        if not (red_flag[j]) and red[j][0] < blue[i][0] and red[j][1] < blue[i][1]:
            pair_red_index = j
            break
    if pair_red_index != float('inf'):
        red_flag[pair_red_index] = True
print(red_flag.count(True))
