#!/usr/bin/env python3

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, "input.txt")

def part1(data):
    print("Part 1")
    trees = calculateTrees(data, 3, 1)

    return(trees)

def part2(data):
    print("Part 2")

    total = calculateTrees(data, 1,1)

    sum = calculateTrees(data, 3,1)
    total *=sum

    sum = calculateTrees(data, 5,1)
    total *=sum

    sum = calculateTrees(data, 7,1)
    total *=sum

    sum = calculateTrees(data, 1,2)
    total *=sum

    print("Part 2 Total = {}".format(total))

def calculateTrees(data, x_incr, y_incr):
    # Work out the size of the input data
    numRows = len(data)
    widthRow = len(data[0])
    # Default current position
    x = 0
    y = 0
    # Tree counter
    trees = 0
    for n, line in enumerate(data):

        if( n % y_incr == 0):
            if (line[x % widthRow] == '#'):
                trees += 1

            x += x_incr
            y += y_incr

    print("X={}, Y={} - Total number of trees hit = {}".format(x_incr, y_incr, trees))

    return trees


def main():
    with open(inputfile) as f:
        data = f.read().splitlines()

        part1(data)
        part2(data)

if __name__ == "__main__":
    main()