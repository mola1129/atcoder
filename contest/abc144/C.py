def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(n // i + i)
            if i != n // i:
                divisors.append(n // i + i)
    divisors.sort()
    return divisors


def main():
    n = int(input())
    divs = make_divisors(n)
    res = divs[0]
    print(res - 2)


if __name__ == '__main__':
    main()
