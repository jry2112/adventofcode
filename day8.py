# --- Day 8: Handheld Halting ---
#
# Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the
# in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting
# next to you.
#
# Their handheld game console won't turn on! They ask if you can take a look.
#
# You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should
# be able to fix it, but first you need to be able to run the code in isolation.
#
# The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an
# operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
#
#     acc increases or decreases a single global value called the accumulator by the value given in the argument.
#     For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction,
#     the instruction immediately below it is executed next.
#
#     jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as
#     an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to
#     the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
#
#     nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
#
# For example, consider the following program:
#
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
#
# These instructions are visited in this order:
#
# nop +0  | 1
# acc +1  | 2, 8(!)
# jmp +4  | 3
# acc +3  | 6
# jmp -3  | 7
# acc -99 |
# acc +1  | 4
# jmp -4  | 5
# acc +6  |
#
# First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next
# instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes,
# setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to
# continue back at the first acc +1.
#
# This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to
# run any instruction a second time, you know it will never terminate.
#
# Immediately before the program would run an instruction a second time, the value in the accumulator is 5.
#
# Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the
# accumulator?
#
# To begin, get your puzzle input.

step = 0

data = open('/Users/jadab/PycharmProjects/adventofcode/day8', "r")
raw = data.readlines()
instruction_dict = dict()

# Create dictionary mapping step + instruction to amount
count = 0
for line in raw:
    value = line[:3], int(line[4:])
    instruction_dict[count] = value
    count += 1

print(instruction_dict)

def jmp_command(self, current_step, step_size):
        next_step = int(current_step + step_size)
        return next_step

def acc_command(self, current_step, acc_value, acc_increment):
    new_acc = acc_value + acc_increment
    current_step += 1
    return new_acc, current_step


visited_key_list = [0]

key = 0
acc = 0
for x in range(0, 636):
    command = instruction_dict[key][0]
    increment = instruction_dict[key][1]
    print("current key:", key, "current command:", instruction_dict[key])
    if command == "jmp":
        key += increment
        current_command = instruction_dict[key]
    elif command == "acc":
        acc += increment
        key += 1
        current_command = instruction_dict[key]
    elif command == "nop":
        key += 1
        current_command = instruction_dict[key]

    if key not in visited_key_list:
        visited_key_list.append(key)
    else:
        print(acc)


key = 0
acc = 0
for x in range(0, len(instruction_dict)):
    command = instruction_dict[key][0]
    increment = instruction_dict[key][1]
    print("current key:", key, "current command:", instruction_dict[key])
    if command == "jmp":
        if instruction_dict[key][1] > 0:
            key += increment
            current_command = instruction_dict[key]
        elif instruction_dict[key][1] < 0:
            instruction_dict[key][0] == "nop"
    elif command == "acc":
        acc += increment
        key += 1
        current_command = instruction_dict[key]
    elif command == "nop":
        key += 1
        current_command = instruction_dict[key]

    if key not in visited_key_list:
        visited_key_list.append(key)
    else:
        print(acc)

