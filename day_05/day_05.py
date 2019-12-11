from IntcodeComputer.IntcodeComputer import IntcodeComputer


def intcode_computer(instructions, inp):
    ip = 0

    while True:
        instruction = f'{instructions[ip]:04}'

        opcode = int(instruction[2:])

        if opcode == 99:
            break

        # Input
        if opcode == 3:
            first_param = instructions[ip + 1]
            instructions[first_param] = inp
            ip += 2

        # Output
        elif opcode == 4:
            first_param = instructions[ip + 1]
            print(f'output: {instructions[first_param]}')
            ip += 2

        # Arithmetic and logical ops
        else:
            param_modes = instruction[:2]
            param_mode_a = int(param_modes[-1])
            param_mode_b = int(param_modes[-2])

            first_param = instructions[instructions[ip + 1]] if param_mode_a == 0 else instructions[ip + 1]
            second_param = instructions[instructions[ip + 2]] if param_mode_b == 0 else instructions[ip + 2]
            address = instructions[ip + 3]

            # Add
            if opcode == 1:
                instructions[address] = first_param + second_param
                ip += 4

            # Multiply
            elif opcode == 2:
                instructions[address] = first_param * second_param
                ip += 4

            # Check if not 0
            elif opcode == 5:
                if first_param is not 0:
                    ip = second_param
                else:
                    ip += 3

            # Check if 0
            elif opcode == 6:
                if first_param is 0:
                    ip = second_param
                else:
                    ip += 3

            # Less than
            elif opcode == 7:
                instructions[address] = int(first_param < second_param)
                ip += 4

            # Equals
            elif opcode == 8:
                instructions[address] = int(first_param == second_param)
                ip += 4

            # Error
            else:
                print(f'Something went wrong. Got opcode: {opcode}')
                break

instructions = open('input.txt').read()
computer = IntcodeComputer(instructions, additional_memory_blocks=0, interrupt_mode=False)
computer.input_queue.append(5)
computer.run()
print(computer.output_queue)
