import re
from itertools import combinations


def sub_str_count(sub_str, string):
    count = 0
    found_at = -1

    for i in range(len(string)):
        if i <= found_at:
            continue
        found_at = string[i:].find(sub_str)
        if found_at != -1:
            count += 1
            found_at = found_at + i
        else:
            break
    return count


def minion_game(string):
    kevin_dict = {}
    stuart_dict = {}
    kevin_count = 0
    stuart_count = 0

    # for x, y in combinations(range(len(string) + 1), r=2):
    #     sub_str = string[x:y]
    #     if sub_str[0] in 'AEIOU':
    #         if not kevin_dict.get(sub_str):
    #             kevin_dict[sub_str] = 1
    #             kevin_count += sub_str_count(sub_str, string)
    #     else:
    #         if not stuart_dict.get(sub_str):
    #             stuart_dict[sub_str] = 1
    #             stuart_count += sub_str_count(sub_str, string)
    # Solution from internet
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            kevin_count += len(string) - i
        else:
            stuart_count += len(string) - i

    for i in range(len(string)):
        for j in range(i, len(string)):
            sub_str = string[i:j + 1]
            if sub_str[0] in 'AEIOU':
                if not kevin_dict.get(sub_str):
                    kevin_dict[sub_str] = 1
                    kevin_count += sub_str_count(sub_str, string)
            else:
                if not stuart_dict.get(sub_str):
                    stuart_dict[sub_str] = 1
                    stuart_count += sub_str_count(sub_str, string)

    if stuart_count > kevin_count:
        print(f'Stuart {stuart_count}')
    elif stuart_count < kevin_count:
        print(f'Kevin {kevin_count}')
    else:
        print('Draw')

    # your code goes here


if __name__ == '__main__':
    s = input()
    minion_game(s)