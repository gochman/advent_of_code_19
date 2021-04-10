import math

LOW = 156218
HIGH = 652527


def check_adjacent_digits(n):
    strn = str(n)
    triple = False
    for i in range(len(strn) - 1):
        if i < len(strn) - 2:
            if strn[i] == strn[i + 1]:
                if strn[i + 1] != strn[i + 2]:
                    if triple:
                        triple = False
                    else:
                        return True
                else:
                    triple = True
        else:
            if strn[i - 1] != strn[i] == strn[i + 1]:
                return True

    return False


def check_increase(n):
    n_lst = [int(x) for x in str(n)]

    for i in range (len(n_lst) - 1):
        if n_lst[i] > n_lst[i+1]:
            return False

    return True


# def check_triples(n):
#     strn = str(n)
#     for i in range(len(strn) - 2):
#         if (strn[i] == strn[i + 1]) & (strn[i] == strn[i + 2]):
#             return True
#
#     return False


def main():
    # print(check_adjacent_digits(777788))
    counter = 0
    for num in range(LOW,HIGH + 1):
        if check_adjacent_digits(num) & check_increase(num):
            counter += 1
            print(num)

    print(counter)


if __name__ == "__main__":
    main()