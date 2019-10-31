def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cost = [float('inf')] * n
    cost[0] = 0
    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j < 0:
                break
            else:
                cost[i] = min(cost[i], cost[i - j] + abs(h[i] - h[i - j]))
    print(cost[n - 1])


if __name__ == "__main__":
    main()
