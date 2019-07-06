A,B,T = map(int,input().split())
cnt = 0
while A*cnt < (T+0.5):
    cnt += 1

print((cnt-1)*B)
