import time
from collections import deque
from itertools import permutations

from IntcodeComputer.IntcodeComputer import IntcodeComputer, OutputtedValueInterrupt, EmptyInputInterrupt

test_instructions_01 = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
test_input_01 = (4, 3, 2, 1, 0)
test_answer_01 = 43210
test_instructions_02 = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
test_input_02 = (0, 1, 2, 3, 4)
test_answer_02 = 54321
test_instructions_03 = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
test_input_03 = (1, 0, 4, 3, 2)
test_answer_03 = 65210
test_instructions_04 = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
test_input_03 = (1, 0, 4, 3, 2)
test_answer_03 = 65210


def normal_mode(initial_value, perm, instructions):
    output = initial_value
    computer = IntcodeComputer(instructions, interrupt_mode=False)
    for val in list(perm):
        computer.input_queue = deque([val, output])
        computer.run()
        output = computer.output_queue.pop()
        computer.reset()

    return output

def part_01():
    possibilities = [0, 1, 2, 3, 4]
    perms = [perm for perm in permutations(possibilities)]
    instructions_to_use = open('input.txt').read()

    max_output = 0
    for perm in perms:
        output = normal_mode(0, perm, instructions_to_use)
        if output > max_output:
            max_output = output
    return max_output

print(part_01())

def feedback_mode(perm, prgm):
    computers = list()
    for phase in perm:
        computers.append(IntcodeComputer(prgm, interrupt_mode=True))
        computers[-1].input_queue.append(phase)

    computers[0].input_queue.append(0)

    i = -1
    while True:
        i = (i + 1) % 5
        while not computers[i].finished:
            try:
                computers[i].run()
            except OutputtedValueInterrupt:
                computers[(i + 1) % 5].input_queue.append(computers[i].output_queue[-1])
                continue
            except EmptyInputInterrupt:
                break

        if all(map(lambda x: x.finished, computers)):
            break

    return computers[-1].output_queue.pop()


def part_02():
    program = open('input.txt').read()
    perms = permutations(range(5, 10))

    result = 0
    for perm in perms:
        res = feedback_mode(perm, program)
        if res > result:
            result = res

    return result
print(part_02())
