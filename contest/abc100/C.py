N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    # 2進数に変換
    # 右から1が現れるまでの0の個数を求める
    ans += format(i, 'b')[::-1].find('1')
print(ans)
