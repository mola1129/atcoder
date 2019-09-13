n, m = map(int, input().split())
x = list(map(int, input().split()))


if n >= m:
    # 全ての地点にコマを置ける
    print(0)
else:
    x.sort()
    # 隣り合う地点間の距離を求める
    # ex. 地点:[-100,0,1,5]
    # ans. diff:[100,1,4]
    diff = [x[i + 1] - x[i] for i in range(m - 1)]
    diff.sort()
    # そのなかで削減可能なのは、高々n-1個分
    print(sum(diff[0:m - n]))
