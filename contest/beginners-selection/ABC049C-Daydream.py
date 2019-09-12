S = input()
l = len(S)
w = ["dream", "dreamer", "erase", "eraser"]
flag = 0

while True:
    for i in range(0,4):
        # 後ろからマッチするか確認
        if S[l-len(w[i]):l] == w[i]:
            l -= len(w[i])
            break
        # マッチするものがないフラグ
        elif w[i] == "eraser":
            flag = 1
    # フラグが立ってたらNO
    if flag == 1:
        print("NO")
        break
    # ピッタリ一致したらYES
    elif l == 0:
        print("YES")
        break
