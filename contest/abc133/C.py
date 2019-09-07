<<<<<<< HEAD
l, r = map(int, input().split())
l_mod = l % 2019
r_mod = r % 2019
area = r_mod - l_mod
ans = -1
if area > 0:
    ans = l_mod * (l_mod + 1) % 2019
else:
    ans = 0
print(ans)
=======
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
>>>>>>> 736216006f8854f659bc5e9e7b10cc85f8db1936
