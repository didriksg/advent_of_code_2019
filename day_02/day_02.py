
def intcode_computer(instructions, noun, verb):
    ip = 0
    instructions[1] = noun
    instructions[2] = verb

    while True:
        opcode = instructions[ip]

        if opcode == 99:
            break

        a = instructions[instructions[ip+1]]
        b = instructions[instructions[ip+2]]

        if opcode == 1:
            instructions[instructions[ip+3]] = a + b
            ip += 4
        elif opcode == 2:
            instructions[instructions[ip+3]] = a*b
            ip += 4

    output = instructions[0]

    return output



test_02 = [1,0,0,0,99]
test_02_eo = 2

test_03 = [2,3,0,3,99]
test_03_eo = 6

test_04 = [2,4,4,5,99,0]
test_04_eo = 9801

test_05 = [1,1,1,4,99,5,6,0,99]
test_05_eo = 30

test_02_res = intcode_computer(test_02,0,0)
test_03_res = intcode_computer(test_03,3,0)
test_04_res = intcode_computer(test_04,4,4)
test_05_res = intcode_computer(test_05,1,1)

assert test_02_eo, test_02_res
assert test_03_eo, test_03_res
assert test_04_eo, test_04_res
assert test_05_eo, test_05_res

instructions = [int(d) for d in open('input.txt').read().split(',')]
result = intcode_computer(instructions, 12, 2)
print(result)

