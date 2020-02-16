import itertools
number = list(map(int, input().split()))
ans = []
for i, j, k in itertools.combinations(number, 3):
    ans.append(i + j + k)
ans.sort(reverse=True)
print(ans[2])
