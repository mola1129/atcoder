s = input()
k = int(input())
# 最初の数字から1が連続している部分を把握
# ex. 1111113344
series_one_end = 0
for i in range(len(s)):
    if s[i] == '1':
        series_one_end = int(i + 1)
    else:
        break
if k <= series_one_end:
    # 1の連続範囲内なら1
    print(1)
else:
    print(s[series_one_end])
