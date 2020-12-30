#!/usr/bin/env python3

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

def preamble_set(data, preamble_len):
    # Loop through the data starting at the first item past the preamble
    for i in range(preamble_len, len(data)):

        # Save the value we are trying to match
        target = int(data[i])

        # Default the found flag
        found = False

        # Create a set for the preamble data
        preamble_data = set()
        for j in range(i-preamble_len, i):
            preamble_data.add(int(data[j]))

        # Loop through the preamble data to see if the sum  of two values match the target
        for val in preamble_data:
            if (target - val) in preamble_data:
                found = True
                break

        if found == False:
            print(f'Exception Found. Value = {target}')
            return(target)

    return 0

def part1(data):
    print("Part 1:")

    weakness = preamble_set(data, 25)

    return weakness


def part2(data, weakness):
    print("Part 2:")

    target = int(weakness)

    # Loop through all the elements
    for i in range(len(data)):
        sum = int(data[i])

        # Set the smallest and largest numbers
        smallest = sum
        largest = sum

        # Continue adding the next elements to the sum until we either
        # match the target value, or we blow through the max value.
        for j in range(i+1, len(data)):
            sum += int(data[j])

            if( int(data[j]) < int(smallest)):
                smallest = data[j]

            if(int(data[j]) > int(largest)):
                largest = data[j]

            if(sum == target):
                print(f"Found contiguous data. Smallest {smallest} - Largest {largest} - Sum = {int(smallest) + int(largest)}")

                return(int(smallest) + int(largest))

            elif (sum > target):
                break

    return

def main():
    with open(inputfile) as f:
        data = f.read().splitlines()

        weakness = part1(data)
        sum = part2(data, weakness)

    return

if __name__ == "__main__":
    main()

