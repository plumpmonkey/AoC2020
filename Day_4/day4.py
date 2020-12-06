#!/usr/bin/env python3

import os
import re

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, "input.txt")

def validateNumFields(passport):

    # Valid fields are "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    # "cid" is optional

    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for field in requiredFields:
        if field not in passport.keys():
            return False

    return True

def part1(passports):
    print("Part 1")

    valid = 0

    for passport in passports:
        if validateNumFields(passport) == True:
            valid += 1

    print("Total passports {}".format(len(passports)))
    print("Total Number of valid passports = {}".format(valid))

def validateFields(passport):
    # print("Validating {}".format(passport))

    if("byr" in passport.keys()):
        year = int(passport['byr'])
        if year < 1920 or year > 2002:
            # print("Invalid byr {}".format(passport['byr']))
            return False

    if ("iyr" in passport.keys()):
        year = int(passport['iyr'])
        if year < 2010 or year > 2020:
            # print("Invalid iyr {}".format(passport['iyr']))
            return False

    if ("eyr" in passport.keys()):
        year = int(passport['eyr'])
        if year < 2020 or year > 2030:
            # print("Invalid eyr {}".format(passport['eyr']))
            return False

    if ("hgt" in passport.keys()):
        height = passport['hgt']

        if(height[-2:] == "cm"):
            heightValue = int(height[:-2])
            if(heightValue < 150 or heightValue > 193):
                # print("Invalid hgt {}".format(heightValue))

                return False
        elif(height[-2:] == "in"):
            heightValue = int(height[:-2])
            if (heightValue < 59 or heightValue > 76):
                # print("Invalid hgt {}".format(heightValue))
                return False
        else:
            # print("Invalid hgt {}".format(height))
            return False

    if("hcl" in passport.keys()):
        colour = passport['hcl']

        pattern = re.compile("#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]")
        match = re.search(pattern, colour)

        if not match:
            # print("Invalid hcl {}".format(colour))
            return False

    if("ecl" in passport.keys()):
        validColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if passport['ecl'] not in validColours:
            # print("Invalid ecl {}".format(passport['ecl']))

            return False

    if("pid" in passport.keys()):
        id = passport['pid']

        if len(id) is not 9 or not id.isnumeric():
            # print("Invalid ecl {}".format(passport['pid']))

            return False

    return True

def part2(passports):
    print("Part 2")

    valid = 0

    for passport in passports:
        if validateNumFields(passport) == True:
            if validateFields(passport) == True:
                valid += 1

    print("Total valid passports = {}".format(valid))

def main():
    with open(inputfile) as f:
        data = f.read().splitlines()

        passports = cleanData(data)

        part1(passports)
        part2(passports)

def cleanData(data):
    passports = []
    fields = ''
    # Clean up the data input
    for line in data:
        if (len(line) != 0):
            # Line length non-zero so combine up the fields in the
            # passport entry.
            fields += line

            # Add a space to the line in case there is another line for
            # this passport
            fields += " "

        else:
            # Convert the passport entry to a dictionary
            dict = {}

            # Drop the last space character
            fields = fields[:-1]

            # Split the passport up based on elements
            fields = fields.split(' ')

            # Create a dict from the pairs
            for field in fields:
                pairs = field.split(":")

                dict[pairs[0]] = pairs[1]

            passports.append(dict)
            fields = ''
    return passports


if __name__ == "__main__":
    main()