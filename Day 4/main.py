with open("data.txt", "r") as file: # Open the data file
    data = [i.replace("\n", " ") for i in file.read().split("\n\n")] # Split each passport into diffrent elements and make each of them into 1 line

def get_value(i, serch):
    i = i.replace("\n", " ")
    indx1 = i.find(serch)
    indx2 = i[indx1:].find(" ")

    if i[indx1:].find(" ") == -1:
        res = i[indx1 + 4 :]
    else:
        res = i[indx1 + 4 : indx2 + indx1]

    return res


totalValid = 0 # To store the desired output as an integer
checks = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid") # The feilds to check
for i in data: # Loop over each passport stored in data
    validationLevel = 0 # The amount of conditions met

    for check in checks: # Loop over each check
        if check in i: # Check if the check variable is in the strings
            validationLevel += 1 # Increase the verification level by one

    if validationLevel == len(checks): # Check if all the checks were posetive
        validationLevel = 0 # Reset the validation level

        byr = get_value(i, "byr")
        iyr = get_value(i, "iyr")
        eyr = get_value(i, "eyr")
        hgt = get_value(i, "hgt")
        hcl = get_value(i, "hcl")
        ecl = get_value(i, "ecl")
        pid = get_value(i, "pid")

        if int(byr) < 1920 or int(byr) > 2002 or len(byr) != 4:
            validationLevel += 1
        print(validationLevel, end = " ")

        if int(iyr) < 2010 or int(iyr) > 2020 or len(iyr) != 4:
            validationLevel += 1
        print(validationLevel, end = " ")


        if int(eyr) < 2020 or int(eyr) > 2030 or len(eyr) != 4:
            validationLevel += 1
        print(validationLevel, end = " ")

        if "in" in hgt:
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
                validationLevel += 1
        elif "cm" in hgt:
            if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
                validationLevel += 1
        else:
            validationLevel += 1
        print(validationLevel, end = " ")

        try:
            int(hcl[1:], 16)
            if len(hcl) != 7:
                validationLevel += 1
        except ValueError:
            validationLevel += 1
        print(validationLevel, end = " ")

        if ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            validationLevel += 1
        print(validationLevel, end = " ")

        if not pid.isnumeric() or len(pid) != 9:
            validationLevel += 1
        print(validationLevel)

        # if int(res) < 2020 or int(res) > 2030 or len(res) != 4:
        #     validationLevel += 1

        print(not pid.isnumeric() or len(pid) != 9)
        print(validationLevel)
        if validationLevel == 0:

            totalValid += 1



print(totalValid)
