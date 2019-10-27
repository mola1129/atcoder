import math


def main():
    a, b, x = map(int, input().split())
    # 水平時の高さを求める
    h = x / a ** 2
    rad = 0
    if h >= (b / 2):
        # 高さが半分以上
        # 水のない三角形部分の高さを求める
        u = (a * a * b - x) * 2 / a ** 2
        rad = math.atan(u / a)
    else:
        # 高さが半分以下
        # 水部分の三角形の高さを求める
        u = x / (b * a) * 2
        rad = math.atan(b / u)
    # ラジアンから度数へ変換
    print(math.degrees(rad))


if __name__ == '__main__':
    main()
