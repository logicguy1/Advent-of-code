with open("data.txt", "r") as file: # Open the data file
    data = [i.replace("\n", " ") for i in file.read().split("\n\n")] # Split each passport into diffrent elements and make each of them into 1 line

def get_value(i, serch): # A function used to find values in passports
    i = i.replace("\n", " ") # Replace all newlines with a space
    indx1 = i.find(serch) # Find the first index ( WHere the serch will start from)
    indx2 = i[indx1:].find(" ") # Find the second index

    if indx2 == -1: # CHeck if it could not find an ecsaping space
        res = i[indx1 + 4 :] # Since the value must be at the end we just take it from index1 + 4 to the end
    else: # If indx2 was found
        res = i[indx1 + 4 : indx2 + indx1] # We just return the output normally

    return res # Return the result

totalValid1 = 0 # To store the desired output for part 1 as an integer
totalValid2 = 0 # To store the desired output for part 2 as an integer
checks = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid") # The feilds to check
for i in data: # Loop over each passport stored in data
    validationLevel = 0 # The amount of conditions met

    for check in checks: # Loop over each check
        if check in i: # Check if the check variable is in the strings
            validationLevel += 1 # Increase the verification level by one

    if validationLevel == len(checks): # Check if all the checks were posetive
        validationLevel = 0 # Reset the validation level

        byr = get_value(i, "byr") # Get each of the values
        iyr = get_value(i, "iyr")
        eyr = get_value(i, "eyr")
        hgt = get_value(i, "hgt")
        hcl = get_value(i, "hcl")
        ecl = get_value(i, "ecl")
        pid = get_value(i, "pid")

        if int(byr) < 1920 or int(byr) > 2002 or len(byr) != 4: # Validate Birth Year
            validationLevel += 1 # Increase the validation level by one ( If the passport is valid we want it to be 0 )

        if int(iyr) < 2010 or int(iyr) > 2020 or len(iyr) != 4: # Validate Issue Year
            validationLevel += 1

        if int(eyr) < 2020 or int(eyr) > 2030 or len(eyr) != 4:# Validate Expiration Year
            validationLevel += 1

        # Validate Height
        if "in" in hgt: # Check if the height is in inches
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76: # Check if it is in the limits of 59 - 76
                validationLevel += 1
        elif "cm" in hgt: # Check if the height is in cencimeters
            if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193: # Check if it is in the limits of 150 - 193
                validationLevel += 1
        else:
            validationLevel += 1

        try:
            int(hcl[1:], 16) # Check if the value is a base 16 integer ( Will raise ValueError if not )
            if len(hcl) != 7: # Check if the value has a length of 7 with the '#' so '#123456'
                validationLevel += 1
        except ValueError: # If the value is not a base 16 integer
            validationLevel += 1

        if ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"): # Check if the Eye Color is valid
            validationLevel += 1

        if not pid.isnumeric() or len(pid) != 9: # Check the Passport ID
            validationLevel += 1

        if validationLevel == 0: # If none of the above if statements got triggerd add one to the total valid
            totalValid2 += 1
        totalValid1 += 1 # Increase the total valid for part one

print(totalValid1) # Print the outputs
print(totalValid2)
