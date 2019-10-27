def main():
    n = int(input())
    for a in range(1, 10):
        b = n / a
        if 1 <= b and b <= 9 and b % 1 == 0:
            print('Yes')
            exit()
    print('No')


if __name__ == '__main__':
    main()
