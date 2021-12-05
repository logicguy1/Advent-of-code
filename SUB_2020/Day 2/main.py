with open("data.txt", "r") as file: # Open the data file
    data = [i.strip() for i in file.readlines()] # Remove all newlines in the file

valid1 = 0 # Variabels to keep track of the valid passwords
valid2 = 0
for i in data: # loop over each line in data
    info, passwd = i.split(": ") # Split the line into each data point
    limits, letter = info.split(" ")
    lowr, uppr = limits.split("-")

    letters = len([x for x in passwd if x == letter]) # Get the amount of matches in the password

    if letters >= int(lowr) and letters <= int(uppr): # Check if the amount of matches lies between the lowr and uppr variabels
        valid1 += 1 # Increase the counter by one
    if sum((passwd[int(lowr) - 1] * 1 == letter, passwd[int(uppr) - 1] == letter) * 1) == 1: # Check if only one of the conditions are met
        valid2 += 1 # Increase the counter by one

print(f"Problem 1: {valid1}") # Print the outputs
print(f"Problem 2: {valid2}")
