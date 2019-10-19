def main():
    import bisect
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    # a < b < c とすると、2式は必ず成立し、c < a + b のみ考慮すれば良い
    # つまり　b < c < a + b
    # c < a + b の境界部の発見に2分探索を利用する
    for i in range(n - 1):
        for j in range(i + 1, n):
            k = bisect.bisect_left(l, l[i] + l[j])
            ans += k - (j + 1)
    print(ans)


if __name__ == '__main__':
    main()
