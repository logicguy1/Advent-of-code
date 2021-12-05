with open("data.txt", "r") as file:
    data = file.readlines()

for x in data:
    for y in data:
        if int(x.strip()) + int(y.strip()) == 2020:
            print(int(x.strip()) * int(y.strip()))
