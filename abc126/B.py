S = list(input())
front = int(S[0])*10 + int(S[1])
back = int(S[2])*10 + int(S[3])

if 1 <= front and front <= 12 and 1 <= back and back <= 12:
    print("AMBIGUOUS")
elif 1 <= front and front <= 12:
    print("MMYY")
elif 1 <= back and back <= 12:
    print("YYMM")
else:
    print("NA")
