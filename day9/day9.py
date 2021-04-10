class Parameter:
    def __init__(self, val, mode):
        self._val = val
        self._mode = mode   # 0 is position, 1 is immediate # 2 is relative

    def get_val(self):
        return int(self._val)

    def get_mode(self):
        return int(self._mode)


class Command:
    def __init__(self, op_code, *args):
        self._opcode = op_code
        self._args = args   # a list of Parameters

    def get_op_code(self):
        return self._opcode

    def get_args(self):
        return self._args


class IntcodeComputer:
    def __init__(self):
        with open(r"C:\Yoav's Disk\AdventOfCode\2019\day9\input.txt") as f:
            content = f.read()

        raw_program_list = content.split(",")
        raw_program_list = [int(x) for x in raw_program_list]
        print(raw_program_list)

        self._raw_program = {k: v for k, v in enumerate(raw_program_list)}


        # for i in range(max(self._raw_program)):
        #     self._raw_program.append(0)

        self._raw_index = 0
        self._relative_base = 0

    def execute(self):
        # count = 0
        while self.handle_command():
            # print("handled")
            # print("-------")
            # count+=1
            pass

    def handle_command(self):
        command = self.parse_command()
        # print("Handling command", command.get_op_code())
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
            return Command(opcode, Parameter(first_param_val,first_param_mode),
                           Parameter(second_param_val, second_param_mode), Parameter(third_param_val, third_param_mode))

        elif opcode == '03' or opcode == '04' or opcode == '09':
            first_param_val = self._raw_program[self._raw_index + 1]
            self._raw_index += 2
            return Command(opcode, Parameter(first_param_val,first_param_mode))

        elif opcode == '05' or opcode == '06':
            first_param_val = self._raw_program[self._raw_index + 1]
            second_param_val = self._raw_program[self._raw_index + 2]

            self._raw_index += 3
            return Command(opcode, Parameter(first_param_val,first_param_mode),
                           Parameter(second_param_val, second_param_mode))

        elif opcode == '99':
            return Command(opcode)
        else:
            print("ERROR")


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

        elif opcode == '09':
            self.exec9(command)
            return True

        else:       # opcode 99
            return False

    def exec1or2(self, command):

        parameters = command.get_args()

        operands = [0, 0]
        for i in range(2):
            if parameters[i].get_mode() == 0:
                operands[i] = self._raw_program.get(parameters[i].get_val(),0)
            elif parameters[i].get_mode() == 1:
                operands[i] = parameters[i].get_val()
            elif parameters[i].get_mode() == 2:
                operands[i] = self._raw_program.get(self._relative_base + parameters[i].get_val(),0)

        output_index = 0
        if parameters[2].get_mode() == 0:
            output_index = parameters[2].get_val()
        elif parameters[2].get_mode() == 1: # cannot happen
            output_index = parameters[2].get_val()
        elif parameters[2].get_mode() == 2:
            output_index = self._relative_base + parameters[2].get_val()

        if command.get_op_code() == '01':
            self._raw_program[output_index] = operands[0] + operands[1]
        elif command.get_op_code() == '02':
            self._raw_program[output_index] = operands[0] * operands[1]

    def exec3or4(self, command):
        parameters = command.get_args()
        if command.get_op_code() == '03':
            input_index = 0
            if parameters[0].get_mode() == 0:
                input_index = parameters[0].get_val()
            elif parameters[0].get_mode() == 1:  # cannot happen
                input_index = parameters[0].get_val()
            elif parameters[0].get_mode() == 2:
                input_index = self._relative_base + parameters[0].get_val()

            self._raw_program[input_index] = int(input("Please Enter Input (03 opcode) "))
        elif command.get_op_code() == '04':
            if parameters[0].get_mode() == 0:
                print("OUTPUT: ", self._raw_program.get(parameters[0].get_val(),0))
            elif parameters[0].get_mode() == 1:
                print("OUTPUT: ", parameters[0].get_val())
            elif parameters[0].get_mode() == 2:
                print("OUTPUT: ", self._raw_program.get(self._relative_base + parameters[0].get_val(),0))

    def exec5678(self, command):
        parameters = command.get_args()
        opcode = command.get_op_code()

        if opcode == '05' or opcode == '06':
            operands = [0,0]
            for i in range(2):
                if parameters[i].get_mode() == 0:
                    operands[i] = self._raw_program.get(parameters[i].get_val(), 0)
                elif parameters[i].get_mode() == 1:
                    operands[i] = parameters[i].get_val()
                elif parameters[i].get_mode() == 2:
                    operands[i] = self._raw_program.get(self._relative_base + parameters[i].get_val(),0)

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
                    operands[i] = self._raw_program.get(parameters[i].get_val(), 0)
                elif parameters[i].get_mode() == 1:
                    operands[i] = parameters[i].get_val()
                elif parameters[i].get_mode() == 2:
                    operands[i] = self._raw_program.get(self._relative_base + parameters[i].get_val(), 0)

            output_index = 0
            if parameters[2].get_mode() == 0:
                output_index = parameters[2].get_val()
            elif parameters[2].get_mode() == 1:  # cannot happen
                output_index = parameters[2].get_val()
            elif parameters[2].get_mode() == 2:
                output_index = self._relative_base + parameters[2].get_val()

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

    def exec9(self, command):
        parameter = command.get_args()[0]
        mode = parameter.get_mode()
        if mode == 0:
            self._relative_base += self._raw_program.get(parameter.get_val(),0)
        elif mode == 1:
            self._relative_base += parameter.get_val()
        elif mode == 2:
            self._relative_base += self._raw_program.get(self._relative_base + parameter.get_val(), 0)





def main():
    my_engine = IntcodeComputer()
    my_engine.execute()


if __name__ == "__main__":
    main()
