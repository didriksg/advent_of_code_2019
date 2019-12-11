from collections import deque


def parse_from_string(program):
    return [int(x) for x in program.split(',')]


def parse_instruction(instruction):
    instruction = f'{instruction:05}'
    opcode = int(instruction[-2:])
    modes = [int(mode) for mode in reversed(instruction[:3])]

    return opcode, modes


class BaseInterrupt(Exception):
    pass


class EmptyInputInterrupt(BaseInterrupt):
    pass


class OutputtedValueInterrupt(BaseInterrupt):
    pass


class IntcodeComputer:
    def __init__(self, program: str, additional_memory_blocks: int = 10000, interrupt_mode: bool = True):
        self.function_mapping = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.adjust_relative_base,
            99: self.exit,
        }

        self.instruction_pointer = 0
        self.relative_base = 0
        self.program = program
        self.finished = False
        self.input_queue = deque()
        self.output_queue = deque()
        self.memory = parse_from_string(self.program) + [0] * additional_memory_blocks
        self.interrupt_mode = interrupt_mode

    def reset(self):
        self.memory = parse_from_string(self.program)
        self.input_queue = []
        self.output_queue = []
        self.instruction_pointer = 0
        self.relative_base = 0
        self.finished = False

    def add(self, modes):
        arg_1 = self.memory[self.get_address(modes[0], 1)]
        arg_2 = self.memory[self.get_address(modes[1], 2)]
        address = self.get_address(modes[2], 3)

        self.memory[address] = arg_1 + arg_2
        self.instruction_pointer += 4

    def multiply(self, modes):
        arg_1 = self.memory[self.get_address(modes[0], 1)]
        arg_2 = self.memory[self.get_address(modes[1], 2)]
        address = self.get_address(modes[2], 3)

        self.memory[address] = arg_1 * arg_2
        self.instruction_pointer += 4

    def input(self, modes):
        address = self.get_address(modes[0], 1)

        try:
            self.memory[address] = self.input_queue.popleft()
        except IndexError:
            if self.interrupt_mode:
                raise EmptyInputInterrupt
        else:
            self.instruction_pointer += 2

    def output(self, modes):
        output = self.memory[self.get_address(modes[0], 1)]

        self.output_queue.append(output)
        self.instruction_pointer += 2

        if self.interrupt_mode:
            raise OutputtedValueInterrupt

    def jump_if_true(self, modes):
        arg_1 = self.memory[self.get_address(modes[0], 1)]
        arg_2 = self.memory[self.get_address(modes[1], 2)]

        if arg_1 != 0:
            self.instruction_pointer = arg_2
        else:
            self.instruction_pointer += 3

    def jump_if_false(self, modes):
        arg_1 = self.memory[self.get_address(modes[0], 1)]
        arg_2 = self.memory[self.get_address(modes[1], 2)]

        if arg_1 == 0:
            self.instruction_pointer = arg_2
        else:
            self.instruction_pointer += 3

    def less_than(self, modes):
        arg_1 = self.memory[self.get_address(modes[0], 1)]
        arg_2 = self.memory[self.get_address(modes[1], 2)]
        address = self.get_address(modes[2], 3)

        self.memory[address] = int(arg_1 < arg_2)
        self.instruction_pointer += 4

    def equals(self, modes):
        arg_1 = self.memory[self.get_address(modes[0], 1)]
        arg_2 = self.memory[self.get_address(modes[1], 2)]
        address = self.get_address(modes[2], 3)

        self.memory[address] = int(arg_1 == arg_2)
        self.instruction_pointer += 4

    def adjust_relative_base(self, modes):
        arg_1 = self.memory[self.get_address(modes[0], 1)]

        self.relative_base += arg_1
        self.instruction_pointer += 2

    def exit(self, modes):
        self.finished = True

    def get_address(self, mode, param):
        # Position mode
        if mode == 0:
            return self.memory[self.instruction_pointer + param]
        # Immediate mode
        elif mode == 1:
            return self.instruction_pointer + param
        # Relative mode
        elif mode == 2:
            return self.memory[self.instruction_pointer + param] + self.relative_base
        else:
            raise Exception(f'Param mode {mode} not recognised.')

    def run(self):
        while not self.finished:
            instruction = self.memory[self.instruction_pointer]
            opcode, modes = parse_instruction(instruction)

            function = self.function_mapping[opcode]
            function(modes)
