n = int(input())
for i in range(n):
    t,x,y=map(int,input().split())
    if (x + y) > t or (x + y + t) % 2:
        print("No")
        exit()
print("Yes")

# N = int(input())
# t = [0]*(N+1)
# x = [0]*(N+1)
# y = [0]*(N+1)
# t[0] = x[0] = y[0] = 0
# # 入力値を保存
# for i in range(0,N):
#     t[i+1],x[i+1],y[i+1] = map(int, input().split())
# # tを差分で保存
# for i in range(0,N):
#     t[i+1] = t[i+1] - t[i]
#
# for i in range(0,N):
#     # 目的地に到着するために最低限必要なtを求める(cost)
#     cost = abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
#     # tが足りないとき・costとt[i]の偶奇が一致しないときは到達不可
#     if t[i+1] < cost:
#         print("No")
#         break
#     elif t[i+1] > cost:
#         if cost % 2 != t[i+1] % 2:
#             print("No")
#             break
#
#     # 全部終わったらYes
#     if i == N-1:
#         print("Yes")
