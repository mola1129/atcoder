s = input()
t = input()
candidate = ['a', 't', 'c', 'o', 'd', 'e', 'r']
for i in range(len(s)):
    if s[i] != t[i]:
        if s[i] != '@' and t[i] != '@':
            print('You will lose')
            exit()
        if s[i] == '@' and t[i] != '@' and not (t[i] in candidate):
            print('You will lose')
            exit()
        if s[i] != '@' and t[i] == '@' and not (s[i] in candidate):
            print('You will lose')
            exit()
print('You can win')
