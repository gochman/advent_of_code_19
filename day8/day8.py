import numpy as np

class Layer:
    def __init__(self, width, height, content):
        self._width = width
        self._height = height
        self._content = content

    def count_num_in_content(self, num):
        count = 0
        for c in self._content:
            if c == str(num):
                count += 1

        return count

    def at(self,i,j):
        return self._content[25 * i + j]




# def part1():
#     with open(r"C:\Yoav's Disk\AdventOfCode\2019\day8\input.txt") as f:
#         image_data = f.read()
#
#     layer_data_list = [image_data[i:i + 150] for i in range(0, len(image_data), 150)]
#
#
#
#     layers = []
#
#     for layer_data in layer_data_list:
#         # print("Size for layer_data: ", len(layer_data))
#         layers.append(Layer(25,6,layer_data))
#
#     fewest_zeros = 151
#     fewest_zeros_layer = 0
#     for c,layer in enumerate(layers):
#         print("Analyzing Layer ", c)
#         count = layer.count_num_in_content(0)
#         if count < fewest_zeros:
#             fewest_zeros = count
#             fewest_zeros_layer = layer
#
#     print("result: ",fewest_zeros_layer.count_num_in_content(1) * fewest_zeros_layer.count_num_in_content(2))


def main():
    with open(r"C:\Yoav's Disk\AdventOfCode\2019\day8\input.txt") as f:
        image_data = f.read()

    layer_data_list = [image_data[i:i + 150] for i in range(0, len(image_data), 150)]

    layers = []

    for layer_data in layer_data_list:
        # print("Size for layer_data: ", len(layer_data))
        layers.append(Layer(25,6,layer_data))

    image = [[2] * 25 for i in range(6)]

    for c,layer in enumerate(layers):
        print("Analyzing Layer ", c)

        for i in range(6):
            for j in range(25):
                if image[i][j] == 2:
                    image[i][j] = int(layer.at(i,j))

    print("Printing result...")
    # print(np.matrix(image))

    for row in image:
        for n in row:
            if n == 1:
                print("■", end="")      # White
            else:
                if n == 0:
                    print(" ", end="")  # Black

        print("")

    # print("test")
    # image2 = [[2] * 25 for i in range(6)]
    # bool = True
    # for row in image2:
    #     for n in row:
    #         if bool:
    #             print("", end="")
    #         else:
    #             print("*, end = """)
    #
    #     print("")


if __name__ == "__main__":
    main()
