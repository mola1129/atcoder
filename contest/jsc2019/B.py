import copy


# k = 1の場合の転倒数を求める
def bubble_sort(A):
    cnt = 0
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                cnt += 1
    return cnt


n, k = map(int, input().split())
a = list(map(int, input().split()))
# aはソートされてしまうので、元の並びを複製する
b = copy.deepcopy(a)
# k = 1の場合の転倒数が初項となる等差数列
initial = bubble_sort(a)
ans = initial
bigger = [0] * n
# bigger[i]: リストaに含まれる要素1つに着目した際に、その要素よりも小さい要素の個数
# ex. a = [1,3,4] のとき、 bigger[1] = 1
# 3より小さいのは1のみであるため。
for i in range(n):
    cnt = 0
    for j in b:
        if b[i] > j:
            cnt += 1
    bigger[i] = cnt
# biggerの合計が公差となる
d = sum(bigger)
# 等差数列の和の公式
ans = k * (2 * initial + d * (k - 1)) // 2
print(ans % (10 ** 9 + 7))
