s = input()
for i in range(2 ** 3):
    formula = s[0]
    for j in range(3):
        if (i >> j) & 1:
            formula += "+"
        else:
            formula += "-"
        formula += s[j + 1]
    if eval(formula) == 7:
        print(formula + "=7")
        exit()
