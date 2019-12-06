N = int(input())
a = list(map(int, input().split()))
print(sum(a) - N)

# 別解(回りくどい)
# import fractions


# def lcm(x, y):
#     return (x * y) // fractions.gcd(x, y)


# N = int(input())
# a = list(map(int, input().split()))
# lcm_ans = a[0]
# for i in range(1, N):
#     lcm_ans = lcm(lcm_ans, a[i])
# ans = 0
# for i in range(N):
#     ans += (lcm_ans - 1) % a[i]
# print(ans)
