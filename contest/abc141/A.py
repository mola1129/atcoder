s = input()
weather = ['Sunny', 'Cloudy', 'Rainy', 'Sunny']
for i in range(3):
    if s == weather[i]:
        print(weather[i + 1])
        break
