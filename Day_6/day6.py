#!/usr/bin/env python3

import os
from collections import Counter

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

def part1(data):
    print("Part 1:")

    sum = 0
    for record in data:

        cleanRecord = record.replace(" ","")

        charSet = set()
        for char in cleanRecord:
            charSet.add(char)

        sum += len(charSet)

    print("Total sum = {}".format(sum))

    return sum

def part2(data):
    print("Part 2:")

    # Convert the data into a list of groups
    # EG - [['ltbriofs', 'bitolfsr', 'olitfrbs', 'sbirloft', 'sbrftiol'], ['erlnjxsqaygzo', 'eznagxlqjry', 'znelyrjaqgx', 'ynxelzgrjaq']...]
    groups = [group.split() for group in data]

    sum = 0

    for group in groups:
        groupSize = len(group)

        # Get counts of the letters
        # EG - Counter({'l': 5, 'f': 5, 'a': 5, 'x': 5, 'i': 2, 'k': 1, 'c': 1, 'm': 1})
        counts = Counter("".join(group))

        # Convert the counter object to a list. then count the number
        # of entries in the list that match the group size
        sum += (list(counts.values()).count(groupSize))

    print("Part 2 total - {}".format(sum))

    return

def cleanData(data):

    # Clean the data so each group record is on one line.
    # Each member of the group is deliminated by a "space"
    cleanedData = []

    record = ''
    for line in data:
        if(len(line) != 0):
            record += " " + line
        else:
            cleanedData.append(record.strip())
            record = ''

    return cleanedData

def main():
    with open(inputfile) as f:
        data = f.read().splitlines()

        # Clean the data so all groups data is on a single line.
        cleaned = cleanData(data)

        part1(cleaned)
        part2(cleaned)


    return

if __name__ == "__main__":
    main()

