#!/usr/bin/env python3

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def convertStringToBinary(string):
    binaryString = ''
    for char in string:
        if char == 'B' or char == 'R':
            binaryString += "1"
        else:
            binaryString += "0"
    return binaryString


def seatID(line):
    row = int(convertStringToBinary(line[:7]), 2)
    column = int(convertStringToBinary(line[-3:]), 2)
    seatdID = row * 8 + column
    return seatID

def part1(data):
    print("Part 1:")

    maxSeatID = 0

    for line in data:
        id = seatID(line)

        if id > maxSeatID:
            maxSeatID = id

    print("Max Seat ID = {}".format(maxSeatID))
    return maxSeatID

def part2(data, maxSeatID):
    print("Part 2:")

    # Create a set of Seat IDs
    ids = set()
    seat = 0

    for line in data:
        ids.add(seatID(line))

    for i in range(maxSeatID):
        if i not in ids and i-1 in ids and i+1 in ids:
            seat = i
            print("My seat is {}".format(i))
            break

    return seat

def main():
    with open(inputfile) as f:
        data = f.read().splitlines()

        maxSeatID = part1(data)
        part2(data, maxSeatID)

    return

if __name__ == "__main__":
    main()

