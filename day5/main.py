import math

def search(hig, data):
    num = hig / 2
    div = num / 2

    for i in data:
        # print(i, div, rowId)
        if i == ">":
            num -= div
        elif i == "<":
            num += div

        div = div / 2

    return round(num)

def get_seat(inp):
    row, col = inp[:7], inp[7:]

    rowId = search(127, row.replace("F", ">").replace("B", "<"))
    colId = search(7, col.replace("L", ">").replace("R", "<"))

    return rowId * 8 + colId

with open("data.txt", "r") as file:
    data = file.readlines()

seatIds = []

maxNum = 0
for i in data:
    seatId = get_seat(i.strip())
    if seatId > maxNum:
        maxNum = seatId

    seatIds.append(seatId)

print("Puzzle 1:", maxNum)

for i in range(min(seatIds), max(seatIds), 1):
    if i not in seatIds:
        print("Puzzle 2:", i)
