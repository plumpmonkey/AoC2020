#!/usr/bin/env python3

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

# Program Counter
pc = 0

# Accumulator
acc = 0

# Executes the individual instruction. Updating the PC and ACC
def runInstruction(line):

    global acc
    global pc

    instruction, offset = line.split()

    if instruction == 'nop':
        pc += 1
    elif instruction == 'acc':
        pc += 1
        acc += int(offset)
    elif instruction == 'jmp':
        pc += int(offset)
    else:
        print("Invalid instruction {}".format(line))

    return

# Runs one instance of the program. Returns False if a
# loop is detected. Or returns True if runs to completion.
def runProgram(data):

    global pc
    global acc

    pc = 0
    acc = 0

    # Set containing PC's that we have executed
    executed = set()

    while pc not in executed and pc < len(data):
        executed.add(pc)

        runInstruction(data[pc])

    if(pc >= len(data)):
        return True
    else:
        return False

def part1(data):
    print("Part 1:")

    global acc
    global pc

    status = runProgram(data)

    if status == False:
        print("STOPPED due to infinite loop")

    print("ACC at loop is {} - PC at loop is {}".format(acc, pc))

    return


def part2(data):
    print("Part 2:")

    # Loop through each of the instructions.
    # if the instruction is 'acc', skip this run.
    # If its jmp or nop, flip the instruction and
    # test if it executed to completion
    # If not, restore the original instruction before
    # continuing the loop.
    for attempt, entry in enumerate(data):
        instruction, offset = entry.split()

        if instruction == 'acc':
            continue
        elif instruction == 'jmp':
            data[attempt] = 'nop ' + offset
        else:
            data[attempt] = 'jmp ' + offset

        status = runProgram(data)

        data[attempt] = instruction + " " + offset

        if status == True:
            print("Terminated on completion- ACC = {}".format(acc))

    return

def main():
    with open(inputfile) as f:
        data = f.read().splitlines()

        part1(data)
        part2(data)

    return

if __name__ == "__main__":
    main()

