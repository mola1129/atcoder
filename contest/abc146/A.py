s = input()
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for i in range(7):
    if s == week[i]:
        print(7 - i)
        break
