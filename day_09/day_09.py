import time

from IntcodeComputer.IntcodeComputer import IntcodeComputer

test_program_01 = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
test_program_02 = '1102,34915192,34915192,7,4,7,99,0'
test_program_03 = '104,1125899906842624,99'
program = open('input.txt').read()

computer_01 = IntcodeComputer(test_program_01, additional_memory_blocks=100, interrupt_mode=False)
computer_02 = IntcodeComputer(test_program_02, additional_memory_blocks=10, interrupt_mode=False)
computer_03 = IntcodeComputer(test_program_03, additional_memory_blocks=10, interrupt_mode=False)
computer_04 = IntcodeComputer(program, additional_memory_blocks=1000, interrupt_mode=False)

computer_04.input_queue.append(2)

computer_01.run()
print(computer_01.output_queue)
computer_02.run()
print(computer_02.output_queue)
computer_03.run()
print(computer_03.output_queue)
start = time.time()
computer_04.run()
print(time.time()-start)
print(computer_04.output_queue)
