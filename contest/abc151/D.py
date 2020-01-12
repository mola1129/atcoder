def main():

    from collections import deque
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    cost = [[600] * w for _ in range(h)]
    nb = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    ans = 0

    def bfs(sx, sy):
        q = deque([(sx, sy)])
        cost[sx][sy] = 0
        value = 0
        while q:
            x, y = q.popleft()
            for dx, dy in nb:
                nx = x + dx
                ny = y + dy
                if 0 <= nx and nx < h and 0 <= ny and ny < w and s[nx][ny] == "." and cost[nx][ny] == 600:
                    q.append((nx, ny))
                    cost[nx][ny] = cost[x][y] + 1
                    value = max(value, cost[nx][ny])
        return value

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                cost = [[600] * w for _ in range(h)]
                tmp = bfs(i, j)
                ans = max(tmp, ans)

    print(ans)


if __name__ == "__main__":
    main()
