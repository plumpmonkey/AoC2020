#!/usr/bin/env python3

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

def part1(data):
    print("Part 1:")
    correct_pw_count = 0

    for line in data:
        # Example PW line
        # 2-4 r: prrmspx
        #
        # 2-4 == min/max count of char
        # r = char
        # prrmspx = pw string
        #
        # Split the line into sections based on space delimiter
        split = line.split(" ")

        # Get the rule min/max value by splitting the line based on a dash
        rule = split[0].split("-")
        # Convert them to values
        min_val = int(rule[0])
        max_val = int(rule[1])

        # Store the letter, which is the first character only
        letter = split[1][0]

        # save the password
        password = split[2]

        # Count the number of times the letter is in the string
        frequency = password.count(letter)

        if frequency in range(min_val, max_val +1):
            correct_pw_count += 1

    print("Total correct passwords == {}".format(correct_pw_count))

    return (correct_pw_count)

def part2(data):
    print("Part 2:")

    correct_pw_count = 0

    for line in data:
        # Split the line into sections based on space delimiter
        split = line.split(" ")

        # Get the rule min/max value by splitting the line based on a dash
        rule = split[0].split("-")
        # Convert them to values
        index1 = int(rule[0]) - 1
        index2 = int(rule[1]) - 1

        # Store the letter, which is the first character only
        letter = split[1][0]

        # save the password
        password = split[2]

        if(password[index1] == letter):
            if(password[index2] != letter):
                correct_pw_count += 1
        elif (password[index2] == letter):
                correct_pw_count += 1

    print("Total correct passwords == {}".format(correct_pw_count))

    return(correct_pw_count)

def main():
    with open(inputfile) as f:
        data = f.read().splitlines()

        assert part1(data) == 467
        assert part2(data) == 441

    return

if __name__ == "__main__":
    main()

