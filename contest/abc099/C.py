def main():
    # 1回の操作で引き出す可能性のある金額リスト
    cash = [1]
    n = int(input())
    # nを超えない範囲で6,9の累乗を追加する
    for i in range(1, n):
        if 6 ** i > n:
            break
        cash.append(6 ** i)
    for i in range(1, n):
        if 9 ** i > n:
            break
        cash.append(9 ** i)
    cash.sort()
    # ans[i]: i円ちょうど引き出すのに必要な操作の最小回数
    ans = [float('inf')] * (n + 1)
    ans[0] = 0
    for i in range(1, n + 1):
        for j in cash:
            if i - j < 0:
                break
            else:
                ans[i] = min(ans[i], ans[i - j] + 1)
    print(ans[n])


if __name__ == "__main__":
    main()
