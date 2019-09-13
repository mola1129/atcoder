def main():
    l, r = map(int, input().split())
    # mod値の取りうる範囲を考える
    rng = r - l
    ans = float("inf")
    # 最大の取りうる範囲は 0 ~ 2018
    if rng >= 2018:
        ans = 0
    else:
        # 範囲を狭めると、全探索可能
        for i in range(l, r):
            for j in range(i + 1, r + 1):
                ans = min(ans, (i * j) % 2019)
    print(ans)


if __name__ == "__main__":
    main()
