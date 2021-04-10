import math
import copy


class Point:
    def __init__(self,x,y,steps):
        self._x = x
        self._y = y
        self._steps = steps

    def get_dist(self):
        return abs(self._x) + abs(self._y)

    def __eq__(self, other):
        """Overrides the default implementation"""
        return self._x == other._x & self._y == other._y

    def __hash__(self):
        return hash(self._x) + hash(self._y)

# def dist(point):
#     return abs(point[0]) + abs(point[1])


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
                steps += 1
                locations.append(Point(x,y,steps))
        elif command[0] == "U":
            for i in range(0 ,command[1]):
                y += 1
                steps += 1
                locations.append(Point(x,y,steps))

        elif command[0] == "L":
            for i in range(0 ,command[1]):
                x -= 1
                steps += 1
                locations.append(Point(x,y,steps))

        elif command[0] == "D":
            for i in range(0 ,command[1]):
                y -= 1
                steps += 1
                locations.append(Point(x,y,steps))



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
    print(str_program1)
    print(locations1)

    print("2: ")
    print(str_program2)
    print(locations2)

    common = common_elements(locations1, locations2)
    print("Common: ")
    print(common)

    min_distance = common[0].get_dist()
    for point in common:
        if point.get_dist() < min_distance:
            min_distance = point.get_dist()

    print(min_distance)

if __name__ == "__main__":
    main()
