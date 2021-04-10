import math


def calc(mass):
    return math.floor(mass / 3) - 2


def calc_total_fuel(fuel):
    if fuel <= 0:
        return 0

    return fuel + calc_total_fuel(calc(fuel))

def main():
    with open(r"C:\Yoav's Disk\AdventOfCode\2019\day1\input.txt") as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]

    fuels = [calc(x) for x in content]
    fuels = [calc_total_fuel(fuel) for fuel in fuels]

    my_sum = sum(fuels)

    print(my_sum)


if __name__ == "__main__":
    main()
