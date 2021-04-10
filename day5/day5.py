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


class ProgramEngine:
    def __init__(self):
        with open(r"C:\Yoav's Disk\AdventOfCode\2019\day5\input.txt") as f:
            content = f.read()

        self._raw_program = content.split(",")
        self._raw_program = [int(x) for x in self._raw_program]

        self._raw_index = 0

    def execute(self):
        while self.handle_command():
            print("handled")

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
            print("ERROR")

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
            self._raw_program[parameters[0].get_val()] = int(input("Please Enter Input (03 opcode) "))
        elif command.get_op_code() == '04':
            if parameters[0].get_mode() == 0:
                print("OUTPUT: ", self._raw_program[parameters[0].get_val()])
            else:
                print("OUTPUT: ", parameters[0].get_val())

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


def main():
    my_engine = ProgramEngine()
    my_engine.execute()


if __name__ == "__main__":
    main()
