def main():
    a, b = map(int, input().split())
    if 1 <= a and a <= 9 and 1 <= b and b <= 9:
        print(a * b)
    else:
        print(-1)


if __name__ == '__main__':
    main()
