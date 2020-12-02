import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

def part1(data):

    print("Part 1:")
    found = False

    for line in data:
        first_number = int(line)

        if(first_number > 2020):
                continue

        for index, line_2 in enumerate(data):

            second_number = int(line_2)

            if (first_number + second_number == 2020):
                solution = first_number * second_number
                print("Solution 1 Found: {} * {} = {}".format(first_number, second_number, solution))
                return(solution)

def part2(data):
    print("Part 2:")
    found = False

    for line in data:
        first_number = int(line)

        if (first_number > 2020):
            continue

        for index, line_2 in enumerate(data):
            second_number = int(line_2)

            if( first_number + second_number > 2020):
                continue

            for index2, line_3 in enumerate(data):
                third_number = int(line_3)

                # print("1: {} 2: {} 3: {}".format(first_number, second_number, third_number))

                if(first_number + second_number + third_number == 2020):
                    solution = first_number * second_number * third_number
                    print("Solution 2 Found: {} * {} * {} = {}".format(first_number, second_number, third_number, solution))
                    return (solution)

                if(first_number + second_number + third_number > 2020):
                    continue

def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        assert part1(data) == 987339
        assert part2(data) == 259521570
if __name__ == "__main__":
    main()