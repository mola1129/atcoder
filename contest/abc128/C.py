N,M = map(int, input().split())
connect = [[0,0,0]]
on_off = [0]*(N+1)
result = 0
for _ in range(M):
    k = list(map(int, input().split()))
    connect.append(k[1:])
p = list(map(int, input().split()))

for cnt in range(0,2**N):
    bin_str = list(format(cnt, 'b'))
    i = len(on_off)-len(bin_str)
    for num in bin_str:
        on_off[i] = int(num)
        i += 1
    for i in range(1,M+1):
        total = 0
        for j in connect[i]:
            total += on_off[j]
        if total % 2 != p[i-1]:
            break
        elif i == M:
            result += 1
print(result)
