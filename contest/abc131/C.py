import fractions
def lcm(x, y):
    return (x * y) // fractions.gcd(x,y)

A,B,C,D = map(int, input().split())
E = lcm(C,D)
cnt_C = 0
cnt_D = 0
cnt_E = 0
if A % C == 0:
    cnt_C += 1
if A % D == 0:
    cnt_D += 1
if A % E == 0:
    cnt_E += 1

diff = B-A
cnt_C += (diff+A%C)//C
cnt_D += (diff+A%D)//D
cnt_E += (diff+A%E)//E

print(B-A+1-cnt_C-cnt_D+cnt_E)
