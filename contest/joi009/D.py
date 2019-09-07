import itertools
n = int(input())
k = int(input())
card = [int(input()) for _ in range(n)]
# 重複は無視するので、集合を考える
integers = set()

# nPkの順列
for select in itertools.permutations(card, k):
    num = ""
    for i in select:
        num += str(i)
    num = int(num)
    # 集合に加える
    # 同じものがある場合は追加されない
    integers.add(num)
print(len(integers))
