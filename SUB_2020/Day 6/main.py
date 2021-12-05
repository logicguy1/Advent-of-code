with open("data.txt", "r") as file:
    data = file.read().split("\n\n")

total = 0
total2 = 0
for i in data:
    i = i.strip()
    y = "".join(i.split("\n"))
    occurences = []
    for x in y:
        if x not in occurences:
            occurences.append(x)

    total += len(occurences)

    y2 = i.split("\n")
    for y in occurences:
        tempTotal = 0
        for x in y2:
            if y in x:
                tempTotal += 1
        if tempTotal == len(y2):
            total2 += 1

print("Puzzle 1:", total)
print("Puzzle 2:", total2)
