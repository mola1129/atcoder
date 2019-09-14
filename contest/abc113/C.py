def main():
    from collections import defaultdict
    dd = defaultdict(str)
    n, m = map(int, input().split())
    keys = []
    atcoder = [[] for _ in range(n)]
    for i in range(m):
        p, y = map(int, input().split())
        # 入力を辞書キーとする
        # 6桁:県番号 10桁:年 = 16桁
        key_p = str(p).zfill(6)
        key_y = str(y).zfill(10)
        keys.append(key_p + key_y)
        # 県ごとに分けて年を追加していく
        p -= 1
        atcoder[p].append(y)
    for i in range(n):
        # 昇順にソート
        atcoder[i].sort()
        key_i = str(i + 1).zfill(6)
        for index, j in enumerate(atcoder[i]):
            # 16桁:(県番号+年)をキーとして、12桁:(県番号＋昇順)の番号を登録
            key_index = str(index + 1).zfill(6)
            key_j = str(j).zfill(10)
            dd[key_i + key_j] = key_i + key_index
    # 出力
    for k in keys:
        print(dd[k])


if __name__ == "__main__":
    main()
