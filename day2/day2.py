import math
import copy


def part1():
    with open(r"C:\Yoav's Disk\AdventOfCode\2019\day2\input2.txt") as f:
        content = f.read()

    base_program = content.split(",")
    base_program = [int(x) for x in base_program]



    for noun in range(0,100):
        for verb in range (0,100):
            program = copy.deepcopy(base_program)
            program[1] = noun
            program[2] = verb

            index = 0
            op_code = base_program[index]
            while op_code != 99:
                operand1_index = program[index + 1]
                operand2_index = program[index + 2]
                output_index = program[index + 3]

                if op_code == 1:
                    program[output_index] = program[operand1_index] + program[operand2_index]
                elif op_code == 2:
                    program[output_index] = program[operand1_index] * program[operand2_index]

                index = index + 4
                op_code = program[index]

            # print(program)

            if program[0] == 19690720:
                print("Yay! Noun is", program[1], "And Verb is ", program[2])
                print("Thus, final answer is: " , 100 * noun + verb)


def main():
    part1()



if __name__ == "__main__":
    main()
