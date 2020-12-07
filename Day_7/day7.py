#!/usr/bin/env python3

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

def parse_rules(data):

    # Create a dictionary of bags, with a list of sub bags
    bag_rules = {}
    for rule in data:
        outerBag, contents = rule.split(" bags contain ")

        bag_rules[outerBag] = []

        if not 'no' in contents:
            inners = ([b.split(" ") for b in contents.split(', ')])

            for bag in inners:
                if len(bag) == 4:
                    bag.pop()

                bag_rules[outerBag] += (["%s %s" % (bag[1], bag[2])] * int(bag[0]))

    return(bag_rules)


def part1(bag_rules):
    print("Part 1:")


    colour_list = find_bags(1, bag_rules, bag_colour="shiny gold")

    print("Total Number of bags that can contain shiny gold = {}".format(len(colour_list)))
    return


def find_bags(depth, bag_rules, bag_colour):
    # print("Depth {} - Find bag {}".format(depth, bag_colour))
    colour_list = set()

    for bag, contents in bag_rules.items():
        if (bag_colour in contents):
            colour_list.add(bag)
            colour_list.update(find_bags(depth + 1, bag_rules, bag))

    return(colour_list)

def count_bags(bag_rules, bag_colour):
    bag_count = 0
    for bag in bag_rules[bag_colour]:
        bag_count += 1;
        bag_count += count_bags(bag_rules, bag)

    return(bag_count)

def part2(bag_rules):
    print("Part 2:")

    print("Total bags = {}".format(count_bags(bag_rules, "shiny gold")))
    return

def main():
    with open(inputfile) as f:
        data = f.read().splitlines()

        bag_rules = parse_rules(data)

        part1(bag_rules)
        part2(bag_rules)


    return

if __name__ == "__main__":
    main()

