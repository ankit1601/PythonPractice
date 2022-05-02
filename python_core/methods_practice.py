# Question Reduce the some to single digit "5555" to "5"
from functools import reduce
from operator import __add__


def convert_str_to_list_int(string_value):
    string_list_int = [int(x) for x in list(string_value)]
    total = reduce(__add__, string_list_int)
    return str(total)


if __name__ == '__main__':
    string = input()
    string_list = list(string)
    str_total = convert_str_to_list_int(string_list)
    while len(str_total) != 1:
        str_total = convert_str_to_list_int(str_total)
    print(str_total)


