N,K = map(int, input().split())
S = list(input())
target = S[K-1]
if target == "A":
    S[K-1] = "a"
elif target == "B":
    S[K-1] = "b"
else:
    S[K-1] = "c"

for str in S:
    print(str, end="")
