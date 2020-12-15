with open("data.txt", "r") as file: # Open the data file
    data = [i.strip() for i in file.readlines()] # Remove all newlines in the file

total = 1 # This stores the output for challange 2 of day 3
for slope in ((1,1), (3,1), (5,1), (7,1), (1,2)): # We loop over each slope
    trees = 0 # Store the total amount of trees met on your walk
    x, y = 0, 0 # Reset out x and y cordinates
    while y != len(data) - 1: # Loop untill we reach the end of the file / forest
        if data[y][x%len(data[0])] == "#": # Check if there is a tree at our location
            trees += 1 # Add one to the counter tree

        x += slope[0]; y += slope[1] # Add our slope to our coridnates

    total *= trees # Multiply the results
    print(slope, trees) # Sho each result one at a time

print(total) # Show the total for part two of the challenge
