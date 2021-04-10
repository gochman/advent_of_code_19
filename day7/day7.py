import itertools

class Parameter:
    def __init__(self, val, mode):
        self._val = val
        self._mode = mode   # 0 is position, 1 is immediate

    def get_val(self):
        return int(self._val)

    def get_mode(self):
        return int(self._mode)


class Command:
    def __init__(self, op_code, *args):
        self._opcode = op_code
        self._args = args   # a list of commands

    def get_op_code(self):
        return self._opcode

    def get_args(self):
        return self._args



class IntcodeComputer:
    def __init__(self, phase_setting, input_signal):
        with open(r"C:\Yoav's Disk\AdventOfCode\2019\day7\input.txt") as f:
            content = f.read()

        self._raw_program = content.split(",")
        self._raw_program = [int(x) for x in self._raw_program]

        self._raw_index = 0

        self._phase_setting = phase_setting
        self._input_signal = input_signal
        self._output_signal = -1

        self._input_counter = 0

    #
    # def get_output_signal(self):
    #     return self._output_signal

    def execute(self):
        while self.handle_command():
            pass
        return self._output_signal

    def handle_command(self):
        command = self.parse_command()
        return self.execute_command(command)

    def parse_command(self):
        code = str(self._raw_program[self._raw_index])
        code_len = len(code)
        to_complete = 5 - code_len

        for i in range(to_complete):
            code = "0" + code

        opcode = code[3:]
        first_param_mode = code[2]
        second_param_mode = code[1]
        third_param_mode = code[0]

        if opcode == '01' or opcode == '02' or opcode == '07' or opcode == '08':
            first_param_val = self._raw_program[self._raw_index + 1]
            second_param_val = self._raw_program[self._raw_index + 2]
            third_param_val = self._raw_program[self._raw_index + 3]

            self._raw_index += 4
            return Command(opcode, Parameter(first_param_val,first_param_mode), Parameter(second_param_val, second_param_mode), Parameter(third_param_val, third_param_mode))

        elif opcode == '03' or opcode == '04':
            first_param_val = self._raw_program[self._raw_index + 1]
            self._raw_index += 2
            return Command(opcode, Parameter(first_param_val,first_param_mode))

        elif opcode == '05' or opcode == '06':
            first_param_val = self._raw_program[self._raw_index + 1]
            second_param_val = self._raw_program[self._raw_index + 2]

            self._raw_index += 3
            return Command(opcode, Parameter(first_param_val,first_param_mode), Parameter(second_param_val, second_param_mode))

        elif opcode == '99':
            return Command(opcode)
        else:
            raise ValueError("BAD OPCODE")

    def execute_command(self, command):
        opcode = command.get_op_code()
        if opcode == '01' or opcode == '02':
            self.exec1or2(command)
            return True

        elif opcode == '03' or opcode == '04':
            self.exec3or4(command)
            return True

        elif opcode == '05' or opcode == '06' or opcode == '07' or opcode == '08':
            self.exec5678(command)
            return True

        else:       # opcode 99
            return False

    def exec1or2(self, command):

        parameters = command.get_args()
        # first operand
        first_operand = 0
        second_operand = 0
        if parameters[0].get_mode() == 0:
            first_operand = self._raw_program[parameters[0].get_val()]
        else:
            first_operand = parameters[0].get_val()

        # second operand
        if parameters[1].get_mode() == 0:
            second_operand = self._raw_program[parameters[1].get_val()]
        else:
            second_operand = parameters[1].get_val()

        output_index = parameters[2].get_val()

        if command.get_op_code() == '01':
            self._raw_program[output_index] = first_operand + second_operand
        elif command.get_op_code() == '02':
            self._raw_program[output_index] = first_operand * second_operand

    def exec3or4(self, command):
        parameters = command.get_args()

        if command.get_op_code() == '03':
            if self._input_counter == 0:
                self._raw_program[parameters[0].get_val()] = int(self._phase_setting)
                self._input_counter += 1
            else:
                self._raw_program[parameters[0].get_val()] = int(self._input_signal)
                


        elif command.get_op_code() == '04':
            if parameters[0].get_mode() == 0:
                # print("OUTPUT: ", self._raw_program[parameters[0].get_val()])
                self._output_signal = self._raw_program[parameters[0].get_val()]
            else:
                # print("OUTPUT: ", parameters[0].get_val())
                self._output_signal = parameters[0].get_val()

    def exec5678(self, command):
        parameters = command.get_args()
        opcode = command.get_op_code()

        if opcode == '05' or opcode == '06':
            operands = [0,0]
            for i in range(2):
                if parameters[i].get_mode() == 0:
                    operands[i] = self._raw_program[parameters[i].get_val()]
                else:
                    operands[i] = parameters[i].get_val()

            if opcode == '05':
                if operands[0] != 0:
                    self._raw_index = operands[1]

            elif opcode == '06':
                if operands[0] == 0:
                    self._raw_index = operands[1]

        elif opcode == '07' or opcode == '08':
            operands = [0,0]
            for i in range(2):
                if parameters[i].get_mode() == 0:
                    operands[i] = self._raw_program[parameters[i].get_val()]
                else:
                    operands[i] = parameters[i].get_val()

            output_index = parameters[2].get_val()

            if opcode == '07':
                if operands[0] < operands[1]:
                    self._raw_program[output_index] = 1
                else:
                    self._raw_program[output_index] = 0

            elif opcode == '08':
                if operands[0] == operands[1]:
                    self._raw_program[output_index] = 1
                else:
                    self._raw_program[output_index] = 0



def get_result_on_permutation(perm):
    # permutation is: (0,2,1,3) for example
    amplifier_a = IntcodeComputer(perm[0], 0)
    a_out = amplifier_a.execute()

    amplifier_b = IntcodeComputer(perm[1], a_out)
    b_out = amplifier_b.execute()

    amplifier_c = IntcodeComputer(perm[2], b_out)
    c_out = amplifier_c.execute()

    amplifier_d = IntcodeComputer(perm[3], c_out)
    d_out = amplifier_d.execute()

    amplifier_e = IntcodeComputer(perm[4], d_out)
    e_out = amplifier_e.execute()

    return e_out


def main():
    all_outputs = []
    phases_permutations = itertools.permutations(range(5,10),5)

    for perm in phases_permutations:
        print("Processing perm: ", perm)
        all_outputs.append(get_result_on_permutation(perm))

    print("Final result is" , max(all_outputs))



if __name__ == "__main__":
    main()
