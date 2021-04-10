import math

class BoardUtilities:
    def __init__(self):
        with open(r"C:\Yoav's Disk\AdventOfCode\2019\day10\input.txt") as f:
            self.raw_content = f.readlines()
        self.raw_content = [x.strip() for x in self.raw_content]

        self._board = []
        for line in self.raw_content:
            self._board.append(list(line))

    def generate_board(self):
        return self._board

    def pretty_print(self):
        for line in self._board:
            for c in line:
                print(c, end=" ")
            print("")


def create_asteroids_list(board):
    asteroids = []  # list of tuples
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j] == '#':
                asteroids.append((i,j))

    return asteroids


# def slope(a,b):
#     if b[0] == a[0]:
#         return math.inf
#     return float((b[0] - a[0]) / (b[1] - a[1]))


def distance(a,b):
    return math.hypot(b[0] - a[0], b[1] - a[1])


def all_points_between(asteroids, asteroid,suspect):
    line_between = []
    for betweener in asteroids:
        if betweener == asteroid or betweener == suspect:
            continue
        if distance(asteroid, suspect) == distance(asteroid, betweener) + distance(betweener, suspect):
            line_between.append(betweener)

    return line_between

def is_line_clear(line,board):
    clear = True
    for point in line:
        if board[point[0]][point[1]] == "#":
            return False

    return True

def main():
    my_utilities = BoardUtilities()
    board = my_utilities.generate_board()
    asteroids = create_asteroids_list(board)
    asteroids_friends_map = {k: 0 for k in asteroids}       # friend means they are visible for each other

    for asteroid in asteroids:
        for suspect in asteroids:
            if asteroid == suspect:
                continue
            line_between = all_points_between(asteroids, asteroid, suspect)     # run time might be a problem double computation
            if is_line_clear(line_between,board):
                asteroids_friends_map[asteroid] += 1

    result = max(asteroids_friends_map,key=asteroids_friends_map.get)

    print("Result is asteroid at:", result[1],",",result[0], " With detected asteroids:", asteroids_friends_map[result])


if __name__ == "__main__":
    main()
