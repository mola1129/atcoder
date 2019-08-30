import sys
input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    L = [[0] * w for _ in range(h)]
    R = [[0] * w for _ in range(h)]
    U = [[0] * w for _ in range(h)]
    D = [[0] * w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if j != 0:
                L[i][j] = L[i][j - 1]
            if s[i][j] == ".":
                L[i][j] += 1
            else:
                L[i][j] = 0
    for i in range(h):
        for j in range(w - 1, -1, -1):
            if j != w - 1:
                R[i][j] = R[i][j + 1]
            if s[i][j] == ".":
                R[i][j] += 1
            else:
                R[i][j] = 0
    for j in range(w):
        for i in range(h):
            if i != 0:
                U[i][j] = U[i - 1][j]
            if s[i][j] == ".":
                U[i][j] += 1
            else:
                U[i][j] = 0
    for j in range(w):
        for i in range(h - 1, -1, -1):
            if i != h - 1:
                D[i][j] = D[i + 1][j]
            if s[i][j] == ".":
                D[i][j] += 1
            else:
                D[i][j] = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                ans = max(ans, L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3)
    print(ans)


if __name__ == "__main__":
    main()
