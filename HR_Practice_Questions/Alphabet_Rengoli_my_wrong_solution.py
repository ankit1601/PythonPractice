import string


def print_rangoli(size):
    row_index = size * 2 - 1
    col_index = row_index * 2 - 1
    alphbets = string.ascii_lowercase[size - 1:0:-1] + string.ascii_lowercase[:size]
    alphbets = "-".join(list(alphbets))
    print(alphbets)
    col_mid_index = col_index // 2
    row_mid_index = row_index // 2

    for i in range(row_index):
        if i <= row_mid_index:
            start_index = col_mid_index - (2 * i + 1)
            end_index = col_mid_index + (2 * i + 1)
            # print(start_index)
            # print(end_index)
        else:
            start_index = col_mid_index - (2 * (row_index - i) - 1)
            end_index = col_mid_index + (2 * (row_index - i) - 1)
            # print(start_index)
            # print(end_index)
        for j in range(col_index):
            if start_index <= j <= end_index:
                print(alphbets[j], end='')
            else:
                if start_index <= j <= end_index:
                    print(alphbets[j], end='-')
                else:
                    print('-', end='')
        print()
    # your code goes here


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
