S = input()
if S[0] == 'A' and S[2:-1].count('C') == 1:
    index_c = S[2:-1].index('C')
    S = S[1:2 + index_c] + S[3 + index_c:]
    if S.islower():
        print('AC')
        exit()
print('WA')
