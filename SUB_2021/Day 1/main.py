import time

DELAY_TIME = .000

with open("data.txt") as file:
    data = [int(i.strip()) for i in file.readlines() if i != "\n"]

##############
#  Part One  #
##############

count = {
        "inc" : 0,
        "dec" : 0,
        "prevVal" : None
        }

for i in data:
    if count["prevVal"] is None:
        print(f"{i} (N/A), inc: {count['inc']} dec: {count['dec']} diff: N/A", end="\r", flush=True)

    elif count["prevVal"] < i:
        count["inc"] += 1
        print(f"{i} (increased), inc: {count['inc']} dec: {count['dec']} diff: {count['prevVal'] - i}", end="\r", flush=True)
    
    elif count["prevVal"] > i:
        count["dec"] += 1
        print(f"{i} (decreased), inc: {count['inc']} dec: {count['dec']} diff: {count['prevVal'] - i}", end="\r", flush=True)
    count["prevVal"] = i

    time.sleep(DELAY_TIME)

print("")

##############
#  Part Two  #
##############

countTwo = {
        "inc" : 0,
        "dec" : 0,
        "prevVal" : None,
        "index" : 0
        }

fetch_val = lambda i: i + data[countTwo['index']] + data[countTwo['index'] + 1]

for i in data:
    countTwo["index"] += 1

    try:
        if countTwo["prevVal"] is None:
            print(f"{i} (N/A), inc: {countTwo['inc']} dec: {countTwo['dec']} diff: N/A", end="\r", flush=True)

        elif countTwo["prevVal"] < fetch_val(i):
            countTwo["inc"] += 1
            print(f"{fetch_val(i)} (increased), inc: {countTwo['inc']} dec: {countTwo['dec']} diff: {countTwo['prevVal'] - fetch_val(i)}", end="\r", flush=True)
    
        elif countTwo["prevVal"] > i + data[countTwo['index']] + data[countTwo['index'] + 1]:
            countTwo["dec"] += 1
            print(f"{fetch_val(i)} (decreased), inc: {countTwo['inc']} dec: {countTwo['dec']} diff: {countTwo['prevVal'] - fetch_val(i)}", end="\r", flush=True)
        
        countTwo["prevVal"] = fetch_val(i)

    except IndexError:
        print(f"Out Of Range{' '*35}", end="\r", flush=True)

    time.sleep(DELAY_TIME)

print("\n")
print("PT1", count, "\nPT2", countTwo)
