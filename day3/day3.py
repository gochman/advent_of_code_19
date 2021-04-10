import math
import copy


def dist(point):
    return abs(point[0]) + abs(point[1])


def str_prog_to_locations(prog):
    commands = []
    for str in prog:
        commands.append((str[0], int(str[1:])))

    locations = []
    x = 0
    y = 0
    steps = 0
    for command in commands:
        if command[0] == "R":
            for i in range(0 ,command[1]):
                x += 1
                locations.append((x, y))
        elif command[0] == "U":
            for i in range(0 ,command[1]):
                y += 1
                locations.append((x,y))
        elif command[0] == "L":
            for i in range(0 ,command[1]):
                x -= 1
                locations.append((x,y))

        elif command[0] == "D":
            for i in range(0 ,command[1]):
                y -= 1
                locations.append((x,y))


    return locations


def common_elements(list1, list2):
    return list(set(list1) & set(list2))


def main():
    with open(r"C:\Yoav's Disk\AdventOfCode\2019\day3\input.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    str_program1 = content[0].split(",")
    str_program2 = content[1].split(",")

    locations1 = str_prog_to_locations(str_program1)
    locations2 = str_prog_to_locations(str_program2)

    print("1: ")
    # print(str_program1)
    print(locations1)

    print("2: ")
    # print(str_program2)
    print(locations2)

    common = common_elements(locations1, locations2)
    print("Common: ")
    print(common)

    min = 1000000
    for point in common:
        sum_steps = locations1.index(point) + 1 + locations2.index(point) + 1
        if sum_steps < min:
            min = sum_steps

    print("Min steps is ", min)


if __name__ == "__main__":
    main()
