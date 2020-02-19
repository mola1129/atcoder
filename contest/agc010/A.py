n = input()
a = list(map(int, input().split()))
# Python: TrueとFalseは0,1と等価
odd_cnt = len([1 for ai in a if ai % 2])
print('YES' if odd_cnt % 2 == 0 else 'NO')
