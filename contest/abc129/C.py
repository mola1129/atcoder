n, m = map(int, input().split())
# 壊れた場所を集合で持っておく
a = {int(input()) for _ in range(m)}
route = [0] * (n + 1)
# route[2]のために初期値は1とする
route[0] = 1
for i in range(1, n + 1):
    # 壊れた場所でないなら、そこまでのルート数を計算
    if not (i in a):
        if i == 1:
            route[i] = 1
        else:
            route[i] = (route[i - 1] + route[i - 2]) % (10 ** 9 + 7)
print(route[n])
