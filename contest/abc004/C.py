import copy
n = int(input())
n %= 30
cards = [1, 2, 3, 4, 5, 6]
candidate = []
candidate.append(cards)
for i in range(6):
    for j in range(1, 6):
        tmp = cards[j]
        cards[j] = cards[j - 1]
        cards[j - 1] = tmp
        b = copy.deepcopy(cards)
        candidate.append(b)
print(*candidate[n], sep='')
