# 問題で提示された関数
def f(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1


s = int(input())
# 初項を追加
a = [s]
index = 1
while True:
    # 関数を適用
    s = f(s)
    index += 1
    # 既に同値が存在するなら終了
    if s in a:
        print(index)
        break
    else:
        # 数列に追加
        a.append(s)
