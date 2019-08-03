s = input()
# + が入る場所の数
num = len(s) - 1
# 合計値
total = 0
# 2のn乗数通りとなる(+を入れる or 入れない)
for i in range(2 ** num):
    formula = s[0]
    for j in range(num):
        # ビット演算で+の入れる or 入れないを表現
        if (i >> j) & 1:
            formula += "+"
        formula += s[j + 1]
    total += eval(formula)
print(total)
